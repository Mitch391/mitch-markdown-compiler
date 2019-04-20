import sys
import checks

if __name__ == '__main__':
    if (sys.argv[0] == sys.argv[-1]):
        print("Please add a file to compile")
    fh, flags = checks.check_all(sys.argv)
    print(fh)
    print(flags)
