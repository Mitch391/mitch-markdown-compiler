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

    def check_for_nodes_word(self, word):
        if word.startswith('**'):
            bold = True
        if word.endswith('**'):
            bold = False

    def check_for_horizontal_rule(self, line):
        if re.match("-+", line):
            return True
        return False

    def check_for_linebreak(self, line):
        if re.match(".*  $", line):
            return True
        return False

    def check_for_bold_in_text(self, text):
        found = re.search("\*\*", text)
        if found:
            self.bold = not self.bold
            return found.span()
        return None

    def add_start_node(self, node):
        self.start_node = node
