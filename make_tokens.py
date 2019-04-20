def make_tokens()


def analyse_word(word):
    print(repr(word))
    dest_token_word = word
    return dest_token_word
    pass


def analyse_line(line):
    dest_token_line = ''

    line = line.rstrip("\n\r")
    line = line.split(" ")
    for word in line:
        analysed_word = analyse_word(word)

        dest_token_line += analysed_word

    return dest_token_line


def loop_through_source(source_file):
    dest_token = ''
    previous_line = ''
    for line in source_file:
        dest_token_line = ''
        analysed_line = analyse_line(line)
        previous_line = line

        dest_token_line += analysed_line

        dest_token += dest_token_line

    return dest_token


def analyse_source(source_file):
    dest_token = loop_through_source(source_file)
    return dest_token
