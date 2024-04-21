#!/usr/bin/python3
""" text-indentation function """


def text_indentation(text):
    """ print text with two new lines after each '.', '?', and ':'

    Args:
        text: the text to print
    Raises:
        TypeError: if text is not a str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = 0
    while x < len(text) and text[x] == ' ':
        x += 1

    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1
