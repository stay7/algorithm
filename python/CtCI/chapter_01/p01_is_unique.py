import collections

# ASCII 문자라고 가정.
# ASCII 문자는 128개


def is_unique_dict(str):
    if len(str) > 128:
        return False

    character_count = {}
    for char in str:
        if char in character_count:
            return False
        character_count[char] = 1
    return True


def is_unique_char(str):
    if len(str) > 128:
        return False

    char_set = [False] * 128
    for char in str:
        if char_set[ord(char)]:
            return False
        char_set[ord(char)] = True
    return True


if __name__ == "__main__":
    test_str = "asdf"
    print(is_unique_dict(test_str))
    print(is_unique_char(test_str))
