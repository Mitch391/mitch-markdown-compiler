import re
import keep_track_of_nodes
import nodes


def analyse_word(word, track_node, node):
    if track_node.check_for_bold_begin(word):
        pass
    dest_node_word = word
    return dest_node_word


def analyse_line(line, track_node, curr_node):
    dest_node_line = []

    if track_node.check_for_horizontal_rule(line):
        node_text = line.strip()
        prev_node = curr_node
        curr_node = nodes.Node("horizontal_rule", node_text, prev_node)
        prev_node.next_node = curr_node

    stripped_line = line.rstrip("\n\r")
    split_line = stripped_line.split(" ")
    for word in split_line:
        analysed_word = analyse_word(word, track_node, curr_node)

        dest_node_line.append(analysed_word)


    if track_node.check_for_linebreak(line):
        node_text = line.strip()
        prev_node = curr_node
        curr_node = nodes.Node("linebreak", node_text, prev_node)
        prev_node.next_node = curr_node

    dest_node_line.append("\n")

    dest_html = " ".join(dest_node_line).strip(" ")

    return curr_node, dest_html


def make_nodes(source_file, track_node, start_node):
    dest_nodes = ''
    previous_line = ''
    curr_node = start_node
    for line in source_file:
        dest_node_line = ''
        curr_node, analysed_line = analyse_line(line, track_node, curr_node)
        previous_line = line

        dest_node_line += analysed_line

        dest_nodes += dest_node_line

    return dest_nodes


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
