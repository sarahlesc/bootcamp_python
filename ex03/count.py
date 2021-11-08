import string


def text_analyzer(*args):
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    if len(args) > 1:
        print("ERROR")
        return
    if len(args) == 1:
        text = args[0]
    if len(args) == 0:
        text = input("What is the text to analyze?\n")
    if (len(text) == 0):
        print("No characher in the text")
        return
    for c in text:
        if c.islower():
            lower += 1
        if c.isupper():
            upper += 1
        if c in string.punctuation:
            punctuation += 1
        if c == ' ':
            spaces += 1
    print("The text contains %i characters:" % len(text))
    print("- %i upper letters" % upper)
    print("- %i lower letters" % lower)
    print("- %i punctuation marks" % punctuation)
    print("- %i spaces" % spaces)
    return
