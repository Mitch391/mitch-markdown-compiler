import sys

sys.path.insert(0, '../make_tree')
import keep_track_of_nodes
import nodes

def open_node(node, markup):
    text = markup
    text += node.text[node.print_level]
    return text 

def close_node(markup):
    text = markup
    return text

def place_mark(node, open_mark, close_mark):
    text = ""
    if node.next_node == []:
        text += open_node(node, open_mark)
        text += close_node(close_mark)
    elif node.print_level < len(node.next_node):
        text += open_node(node, open_mark)
    elif node.print_level == len(node.next_node):
        text += close_node(close_mark)
    return text

def make_heading(node):
    text = "<h1>"
    text += node.text[node.print_level]
    text += "</h1>"
    return text

def make_horizontal_rule(node):
    return "<hr />"

def make_monospace(node):
    text = place_mark(node, "<code>", "</code>")
    return text

def make_italic(node):
    text = place_mark(node, "<i>", "</i>")
    return text

def make_bold(node):
    text = place_mark(node, "<b>", "</b>")
    return text

def make_root(node):
    return node.text[node.print_level]

def make_markup(node):
    return globals()['make_' + node.type_node](node)
    if node.type_node  == "bold":
        return make_bold(node)
    elif node.type_node  == "monopace":
        return make_monospace(node)
    elif node.type_node == "italic":
        return make_italic(node)
    elif node.type_node == "horizontal_rule":
        return make_horizontal_rule(node)
    elif node.type_node == "heading":
        return make_heading(node)
    else:
        return node.text[node.print_level]
    
def get_text(node):
    text = ""
    node.print_level = 0
    for next_node in node.next_node:
        text += make_markup(node)
        node.print_level += 1
        text += get_text(next_node)
    text += make_markup(node)
    return text

def make_html(track_node):
    start_node = track_node.start_node
    text = get_text(start_node)
    print(text)
    return text
