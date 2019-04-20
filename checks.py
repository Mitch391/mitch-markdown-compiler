def check_if_file_exists(fh):
    try:
        source_file = open(fh, 'r')
    except FileNotFoundError:
        print("Target File Not Found")
        exit(1)
    return source_file


def check_if_file_is_md(fh):
    if not fh.lower().endswith('.md'):
        print("Invalid File Type: " + fh)
        print("File must end with .md")
        exit(1)

def check_for_flags(cli_args, fh):
    flags = []
    for cli_arg in cli_args:
        if cli_arg.startswith("-"):
            flags.append(cli_arg)
        else:
            fh = cli_arg
    return fh, flags


def check_all(cli_args):
    fh = None
    fh, flags = check_for_flags(cli_args[1:], fh)

    if fh == None:
        print("Please add a file to compile")
        exit(1)

    check_if_file_exists(fh)
    check_if_file_is_md(fh)
    return fh, flags
