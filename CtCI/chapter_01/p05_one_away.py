def is_one_away(s: str, t: str):
    if(len(s) < len(t)):
        s, t = t, s
    len_diff = len(s)-len(t)

    if len_diff > 1:
        return False
    if len_diff == 0:
        return isOneReplace(s, t)
    return isOneAdd(s, t)


def isOneReplace(s: str, t: str):
    found_diff = False
    for i in range(len(t)):
        if s[i] != t[i]:
            if(found_diff):
                return False
            found_diff = True
        i += 1
    return True


def isOneAdd(s: str, t: str):
    i = bias = 0
    while bias < 2 and i < len(t):
        if s[i+bias] != t[i]:
            bias += 1
            continue
        i += 1
    return bias < 2


if __name__ == "__main__":
    s = "pale"
    t = "pale"
    print(is_one_away(s, t))
