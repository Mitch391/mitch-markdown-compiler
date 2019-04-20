import os
import sys
import checks
import make_tokens

def exists_output_file(file_name_html):
    if os.path.exists(file_name_html):
        text = "Are you sure you want to overwrite "
        text += file_name_html
        text += "? (y/n)"
        answer = input(text)
        if not (answer == "y" or answer == ''):
            exit(1)
        os.remove(file_name_html)


def output_file_standard_head_text(file_name):
    text = "<!DOCTYPE html>\n"
    text += "<html>\n"
    text += "<head>\n"
    text += "<title>" + file_name + "</title>\n"
    text += "<body>\n"
    return text


def output_file_standard_bottom_text():
    text = "</body>\n"
    text += "</html>"
    return text


def make_output_file(file_name, file_type='html'):
    file_name_html = file_name.rstrip(".md")
    file_name_html = file_name_html + ".html"
    exists_output_file(file_name_html)
    dest_file = open(file_name_html, "w+")
    return dest_file

    

if __name__ == '__main__':
    if (sys.argv[0] == sys.argv[-1]):
        print("Please add a file to compile")

    file_name, fh, flags = checks.check_all(sys.argv)

    dest_file = make_output_file(file_name)
    standard_head_text = output_file_standard_head_text(file_name)
    dest_file.write(standard_head_text)

    html = make_tokens.analyse_source(fh)
    
    standard_bottom_text = output_file_standard_bottom_text()
    dest_file.write(standard_bottom_text)
