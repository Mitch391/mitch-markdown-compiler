import re

class Keep_track_of_nodes:
    def __init__(self, heading=False, sub_heading=False, paragraph=False,
                       italic=False, bold=False, monospace=False,
                       bullet_list=False, numbered_list=False,
                       hyperlink=False, blockquote=False):
        self.heading = heading
        self.sub_heading = sub_heading
        self.paragraph = paragraph
        self.italic = italic
        self.bold = bold
        self.monospace = monospace
        self.bullet_list = bullet_list
        self.numbered_list = numbered_list
        self.hyperlink = hyperlink
        self.blockquote = blockquote

    def check_for_horizontal_rule(self, text):
        found = re.search("-+", text)
        if found:
            return found.span()
        return None

    def check_for_monospace_in_text(self, text):
        found = re.search("`", text)
        if found:
            return found.span()
        return None

    def check_for_bold_in_text(self, text):
        found = re.search("\*\*", text)
        if found:
            return found.span()
        return None

    def check_for_italic_in_text(self, text):
        found = re.search("_", text)
        if found:
            return found.span()
        return None

    def add_start_node(self, node):
        self.start_node = node

    def print_values(self):
        #  print("heading", self.heading)
        #  print("sub_heading", self.sub_heading)
        #  print("paragraph", self.paragraph)
        print("italic", self.italic)
        print("bold", self.bold)
