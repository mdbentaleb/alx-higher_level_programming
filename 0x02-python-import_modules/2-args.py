#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    print("{} ".format(arg - 1), end="")
    if arg == 1:
        print("arguments.")
    elif arg > 1:
        if arg == 2:
            print("argument:")
        elif arg > 2:
            print("arguments:")
        for i in range(arg - 1):
            print("{}: {}".format((i + 1), sys.argv[i + 1]))
