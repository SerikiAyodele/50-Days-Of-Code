def mergeStrings(word1: str, word2: str) -> str:
    ptr1, ptr2 = 0, 0
    merged = ""

    while ptr1 < len(word1) and ptr2 < len(word2):
        merged += word1[ptr1] + word2[ptr2]
        ptr1 += 1
        ptr2 += 1

    if len(word1) > len(word2):
        merged += word1[ptr1:]
    elif len(word2) > len(word1):
        merged += word1[ptr2:]
    return merged




