f = open("book.txt", "r", encoding="utf-8")


def cypher(message, book):
    words = message.split()
    # print(words)
    triplets = []
    for word in words:
        match = False
        for c in range(len(book)):
            for l in range(len(book[c])):
                for w in range(len(book[c][l])):
                    # if book[c][l][w].find(word) != -1:
                    if (word == book[c][l][w]):
                        match = True
                        triplets.append((c, l+1, w+1))
                        break
                if match == True:
                    break
            if match == True:
                break
        if match == False:
            print("No se encontró la palabra: "+word+" en el texto.")

    return triplets


def decypher(triplets, book):
    words = []
    for t in triplets:
        words.append(book[t[0]][t[1]-1][t[2]-1])
    return " ".join(words)


text = f.readlines()
pages = []
page = []
for i in range(len(text)):
    if text[i] != '\n':
        try:
            k = int(text[i])
            pages.append(page)
            page = []
        except:
            line = text[i][:-2].split()
            newline = []
            for word in line:
                word = word.replace(',', '')
                word = word.replace('.', '')
                word = word.replace(';', '')
                word = word.replace(':', '')
                newline.append(word)
            page.append(newline)
pages.append(page)

f.close()

print(cypher("dónde están las palabras", pages))
print(decypher([(5, 10, 7), (35, 10, 7), (0, 11, 3), (5, 11, 9)], pages))

print(cypher("qué bonita la caja afirmaba", pages))
print(decypher([(1, 9, 2), (32, 19, 1),
                (0, 15, 11), (5, 1, 4), (1, 1, 5)], pages))
