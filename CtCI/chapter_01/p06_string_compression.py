def string_compression(text):
    compressed = []
    count, base = 0, text[0]
    for char in text:
        if base != char:
            compressed.append(base + str(count))
            count, base = 0, char
        count += 1
    compressed.append(base + str(count))

    # 한 줄에 return하는 방법
    # 1.min에 key를 사용
    # return min(text, ''.join(compressed), key=len)

    # 2.ternary operator 사용
    # return text if len(text) < len(compressed) else ''.join(compressed)
    if len(compressed) < len(text):
        return ''.join(compressed)
    return text


print(string_compression("aabcccccaaa"))
