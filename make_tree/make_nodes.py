import re
import pdb
import keep_track_of_nodes
import nodes
import find_markup

def make_empty_node(curr_node, type_next_node, text, found_span):
    next_node = nodes.Node(type_next_node, [''], curr_node, [])
    next_node.set_text(text[found_span[0]:found_span[1]])
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

def remove_heading_markup(text, first_span):
    found = re.search('\\n=+(\\n|$)', text)
    before_markup = text[:found.span()[0]]
    after_markup = text[found.span()[1]:]
    new_span1 = first_span[0]
    new_span2 = first_span[1] - found.span()[0] + 1
    return (new_span1, new_span2), before_markup + after_markup

def search_for_markup(track_node, curr_node, found):
    found, curr_node, first_span = find_markup.find_first_markup_in_text(track_node, curr_node)

    if not found:
        return False, None

    text = curr_node.get_text()
    markup_type = first_span[2]

    #  if not markup_type == "list_item" and track_node.bullet_list == True and curr_node.type_node == "bullet_list":
    #      curr_node = close_node(curr_node, text, first_span)
    #      track_node.bullet_list = not track_node.bullet_list
    #      return found, curr_node
    #
    if markup_type in ["bold", "italic", "monospace"]:
        track_node_first_span_bool = getattr(track_node, markup_type)
        setattr(track_node, markup_type, not track_node_first_span_bool)
    elif markup_type in ["sub_heading"]:
        sub_heading_level = first_span[3]
        markup_type = "sub_heading" + str(sub_heading_level)
        first_span = (first_span[0], first_span[1])
        make_empty_node(curr_node, markup_type, text, first_span)
        sub_heading_node = curr_node.next_node[-1]
        sub_heading_node.text[0] = sub_heading_node.text[0][sub_heading_level:]
        return found, curr_node
    elif markup_type in ["heading"]:
        first_span, text = remove_heading_markup(text, first_span)
        make_empty_node(curr_node, markup_type, text, first_span)
        return found, curr_node
    else:
        make_empty_node(curr_node, markup_type, text, first_span)
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
    return start_node
