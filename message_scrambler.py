message = "Según un estudio de una universidad inglesa no importa el orden en que las letras estén escritas"


def scramble(message):
    words = message.split()
    scrambled_words = []
    for word in words:
        first_char = word[0]
        last_char = word[-1]
        word = word[1:-1]
        letters = [c for c in word]
        marker = 0
        while marker < len(word):
            if marker+1 < len(word):
                a = letters[marker]
                b = letters[marker+1]
                letters[marker] = b
                letters[marker+1] = a
                marker += 2
            else:
                marker += 1
            # print(letters)

        scrambled_words.append(first_char+"".join(letters)+last_char)

    return " ".join(scrambled_words)


print(scramble(message))
