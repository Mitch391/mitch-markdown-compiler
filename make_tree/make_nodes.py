import re
import keep_track_of_nodes
import nodes
import find_markup

def make_empty_node(curr_node, type_next_node, text, found_span):
    next_node = nodes.Node(type_next_node, [''], curr_node, [])
    curr_node.add_next_node(next_node)
    curr_node.set_text(text[:found_span[0]])
    curr_node.add_text(text[found_span[1]:])

def open_node(curr_node, type_next_node, text, found_span):
    prev_node = curr_node
    prev_node.set_text(text[:found_span[0]])
    curr_node = nodes.Node(type_next_node, [text[found_span[1]:]], prev_node, [])
    prev_node.add_next_node(curr_node)

    return prev_node, curr_node

def close_node(curr_node, text, found_span):
    curr_node.set_text(text[:found_span[0]])
    curr_node = curr_node.prev_node
    curr_node.add_text(text[found_span[1]:])

    return curr_node

def search_for_markup(track_node, curr_node, found):
    found, curr_node, first_span = find_markup.find_first_markup_in_text(track_node, curr_node)

    if not found:
        return False, None

    text = curr_node.get_text()

    if first_span[2] in ["bold", "italic", "monospace"]:
        track_node_first_span_bool = getattr(track_node, first_span[2])
        setattr(track_node, first_span[2], not track_node_first_span_bool)
    else:
        make_empty_node(curr_node, first_span[2], text, first_span)
        return found, curr_node

    if track_node_first_span_bool == False:
        _, curr_node = open_node(curr_node, first_span[2], text, first_span)
    elif track_node_first_span_bool == True:
        curr_node = close_node(curr_node, text, first_span)

    return found, curr_node


def recursive_node_generation(source_file, track_node, curr_node):
    found = True
    while found:
        found = False
        found, curr_node = search_for_markup(track_node, curr_node, found)
    

def analyse_source(source_file, track_node):
    start_node = track_node.start_node
    curr_node = start_node
    recursive_node_generation(source_file, track_node, curr_node)
    return 'html'
