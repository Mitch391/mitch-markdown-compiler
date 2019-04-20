def analyse_word(word):
    print(repr(word))
    dest_html_word = word
    return dest_html_word
    pass


def analyse_line(line):
    dest_html_line = ''

    line = line.rstrip("\n\r")
    line = line.split(" ")
    for word in line:
        analysed_word = analyse_word(word)

        dest_html_line += analysed_word

    return dest_html_line


def loop_through_source(source_file):
    dest_html = ''
    previous_line = ''
    for line in source_file:
        dest_html_line = ''
        analysed_line = analyse_line(line)
        previous_line = line

        dest_html_line += analysed_line

        dest_html += dest_html_line

    return dest_html


def analyse_source(source_file):
    dest_html = loop_through_source(source_file)
    return dest_html
