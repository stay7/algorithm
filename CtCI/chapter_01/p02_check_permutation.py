def check_permutation_sort(s, t):
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    return s == t


def check_permutation_count(s, t):
    if len(s) != len(t):
        return False

    char_array = [0] * 128
    for char in s:
        char_array[ord(char)] += 1
    for char in t:
        char_array[ord(char)] -= 1
        if char_array[ord(char)] < 0:
            return False
    return True


if __name__ == "__main__":
    s = "odg"
    t = "dog"
    print(check_permutation_sort(s, t))
    print(check_permutation_count(s, t))
