def check_if_file_exists(file_name):
    try:
        source_file = open(file_name, 'r')
    except FileNotFoundError:
        print("Target File Not Found")
        exit(1)
    return source_file


def check_if_file_is_md(file_name):
    if not file_name.lower().endswith('.md'):
        print("Invalid File Type: " + file_name)
        print("File must end with .md")
        exit(1)

def check_for_flags(cli_args, file_name):
    flags = []
    for cli_arg in cli_args:
        if cli_arg.startswith("-"):
            flags.append(cli_arg)
        else:
            file_name = cli_arg
    return file_name, flags


def check_all(cli_args):
    file_name = None
    file_name, flags = check_for_flags(cli_args[1:], file_name)

    if file_name == None:
        print("Please add a file to compile")
        exit(1)

    fh = check_if_file_exists(file_name)
    check_if_file_is_md(file_name)
    return file_name, fh, flags
