def solution():
    alpha = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
             "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
             "z": 26, }
    N, M = map(int, input().split(" "))
    valid_words = []
    bit = [[] for _ in range(27)]

    for i in range(N):
        valid_words.append(i)
        word = input()

        for w in word:
            if i not in bit[alpha[w]]:
                bit[alpha[w]].append(i)

    for _ in range(M):
        num, alphabet = input().split(" ")
        if


    print(bit)

    return


solution()
