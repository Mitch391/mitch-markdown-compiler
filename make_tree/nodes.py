class Node:
    def __init__(self, type_node=None, text=[''], prev_node=None, next_node=[]):
        self.type_node = type_node
        self.text = text
        self.prev_node = prev_node
        self.next_node = next_node
        self.level = 0
        self.print_level = 0

    def visualize_node_stream(self):
        node = self
        print_nodes(node, '')

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_text(self):
        text = self.text[self.level]
        return text

    def set_text(self, text):
        self.text[self.level] = text

    def add_text(self, text):
        self.text.append(text)
        self.level += 1

    def get_level(self):
        return self.level

    def add_next_node(self, node):
        self.next_node.append(node)


def print_nodes(node, tabs):
    for next_node in node.next_node:
        print_node(node, tabs)
        node.print_level += 1
        print_nodes(next_node, tabs+'    ')
    print_node(node, tabs)

def print_node(node, tabs):
    print(tabs + node.type_node + ": ", end="")
    print(repr(node.text[node.print_level]))
