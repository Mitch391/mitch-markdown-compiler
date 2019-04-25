import re
import pdb

class Keep_track_of_nodes:
    def __init__(self, paragraph=False, italic=False, bold=False,
                       monospace=False, bullet_list=False, numbered_list=False,
                       hyperlink=False):
        self.paragraph = paragraph
        self.italic = italic
        self.bold = bold
        self.monospace = monospace
        self.bullet_list = bullet_list
        self.numbered_list = numbered_list
        self.hyperlink = hyperlink

    def check_for_list_item_in_text(self, text):
        found = re.search("\s*(\*)|([0-9]\.)", text)
        if found:
            next_newline = re.search("\\n", text)
            if not next_newline:
                next_newline = (len(text),)
            else:
                next_newline = next_newline.span()
            return (found.span()[1], next_newline[0])
        return None

    def check_for_bullet_list_in_text(self, text):
        found_start = re.search('\\n\s*\*\s', text)
        found_end = re.search("\\n\\n", text)
        if found_start:
            if not found_end:
                found_end = (len(text),)
            else:
                found_end = found_end.span()
            return (found_start.span()[0], found_start.span()[1])
        return None

    def check_for_linebreak_in_text(self, text):
        found = re.search(r'  \n', text)
        if found:
            return found.span()
        return None

    def check_for_blockquote_in_text(self, text):
        found = re.search("\\n>", text)
        if found:
            next_newline = re.search("\\n", text[found.span()[1]:])
            if not next_newline:
                next_newline = (len(text),)
            else:
                next_newline = next_newline.span()
            return (found.span()[0], found.span()[1]+next_newline[0])

    def check_for_heading_in_text(self, text):
        found = re.search('\\n=+(\\n|$)', text)
        if found:
            found = (found.span()[0], found.span()[1])
            return found
        return None

    def check_for_sub_heading_in_text(self, text):
        found = re.search("#+", text)
        if found:
            next_newline = re.search("\\n", text[found.span()[1]:])
            if not next_newline:
                next_newline = (len(text),)
            else:
                next_newline = next_newline.span()
            sub_heading_text = (found.span()[0], next_newline[0]+found.span()[1])
            sub_heading_level = found.span()[1] - found.span()[0]
            return sub_heading_text, sub_heading_level
        return None, None

    def check_for_horizontal_rule_in_text(self, text):
        found = re.search("\\n-+\\n", text)
        found_eof = re.search("\\n-+$", text)
        found_sof = re.search("^-+\\n", text)
        found_sof_eof = re.search("^-+$", text)
        if found:
            return (found.span()[0] + 1, found.span()[1] - 1)
        elif found_eof:
            return (found_eof.span()[0] + 1, found_eof.span()[1])
        elif found_sof:
            return (found_sof.span()[0], found_sof.span()[1] - 1)
        elif found_sof_eof:
            return found_sof_eof.span()
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
