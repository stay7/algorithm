def urlify_pythonic(text: str, length: int):
    text = text.rstrip()
    print(text)
    return text.replace(" ", "%20")


def urlify_algo(text, length):
    text = list(text)
    index = len(text)

    for i in reversed(range(length)):
        if text[i] == " ":
            text[index-3: index] = "%20"
            index -= 3
        else:
            text[index - 1] = text[i]
            index -= 1
    return "".join(text[i:])


print(urlify_pythonic("Mr John Smith    ", 13))
print(urlify_algo("Mr John Smith    ", 13))
