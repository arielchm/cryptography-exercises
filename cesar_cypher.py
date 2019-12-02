alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def cypher(message):
    words = message.upper().split()
    new_words = []

    for i in range(len(words)):
        word_copy = words[i]
        frequencies = []

        while len(word_copy) > 0:
            character = word_copy[0]
            n = word_copy.count(character)
            word_copy = word_copy.replace(character, "")
            frequencies.append((character, n))

        frequencies.sort(key=lambda x: x[1], reverse=True)
        stepValue = frequencies[0][1]

        letterVals = [alphabet[stepValue-1]]
        for j in range(len(words[i])):
            if words[i][j] in alphabet:
                jIndex = alphabet.index(words[i][j])
                newIndex = (jIndex + stepValue) % 27

                letterVals.append(alphabet[newIndex])
            else:
                letterVals.append(words[i][j])

        new_words.append("".join(letterVals))

    return " ".join(new_words)


def decypher(secret):
    words = secret.split()
    newwords = []
    # print(words)
    for i in range(len(words)):
        step = alphabet.index(words[i][0])+1
        # print(step)
        word = words[i][1:]
        # print(word)
        letterList = []
        for j in range(len(word)):
            if word[j] in alphabet:
                value = alphabet.index(word[j]) - step
                letterList.append(alphabet[value])
            else:
                letterList.append(word[j])
        # print(letterList)
        newwords.append("".join(letterList))
    return " ".join(newwords)


message = "zaz, YA PIENSES QUE PUEDES O PIENSES QUE NO PUEDES, ESTAS EN LO CIERTO"
print(cypher(message))

secret = "BBCB, AZB BRKGOUGU ARVF BRWGFGU AP BRKGOUGU ARVF AÑP BRWGFGU, BGUVCU AFÑ AMP ADJFSUP"

print(decypher(secret))
