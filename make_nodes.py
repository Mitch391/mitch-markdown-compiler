import re
import keep_track_of_nodes
import nodes

def search_for_markup(text, track_node, curr_node, pointer, found):
    found_bold = track_node.check_for_bold_in_text(text)
    if found_bold and track_node.bold == True:
        prev_node = curr_node
        prev_node.set_text(text[:found_bold[0]])
        curr_node = nodes.Node("bold", [text[found_bold[1]:]], prev_node, [])
        prev_node.add_next_node(curr_node)
        found = True
    elif found_bold and track_node.bold == False:
        curr_node.set_text(text[:found_bold[0]])
        curr_node = curr_node.prev_node
        curr_node.add_text(text[found_bold[1]:])
        found = True

    return found, curr_node


def recursive_node_generation(source_file, track_node, curr_node, pointer):
    found = True
    while found:
        found = False
        text = curr_node.get_text()
        found, curr_node = search_for_markup(text, track_node, curr_node, pointer, found)
    

def analyse_source(source_file, track_node):
    start_node = track_node.start_node
    curr_node = start_node
    pointer = 0
    recursive_node_generation(source_file, track_node, curr_node, pointer)
    return 'html'
