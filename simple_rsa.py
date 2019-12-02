import random
alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
# p, q = map(int, input.split())
# Para números menores a 27
numbers = range(0, 27)


def cypher(plaintext):
    p, q = random.choice(numbers), random.choice(numbers)
    # print(p,q)
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(' ', '')
    cyphertext = ""
    for k in plaintext:
        x = alphabet.index(k)
        # print(x)
        c = (p*x+q) % 27
        y = (p*x+q) // 27
        cyphertext += alphabet[c]+alphabet[y]
    cyphertext += alphabet[p]+alphabet[q]
    return cyphertext


def decypher(cyphertext):
    plaintext = ""
    q = alphabet.index(cyphertext[-1])
    p = alphabet.index(cyphertext[-2])

    # print(p,q)
    cyphertext = cyphertext[:-2]
    while len(cyphertext) != 0:
        a = alphabet.index(cyphertext[0])
        b = alphabet.index(cyphertext[1])
        cyphertext = cyphertext[2:]
        c = int((27 * b+a-q)/p)
        # print(a,b,c)
        plaintext += alphabet[c]
    return plaintext


cyphertext = cypher(input("Input message: "))
print(cyphertext)
print(decypher(cyphertext))
