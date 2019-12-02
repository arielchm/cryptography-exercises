#plaintext = input("Type a message to encode:")
# Convert plaintext to UPPERCASE
plaintext = "HELLO EVERYONE"

n = 3


def cypher(plaintext, n):
    plaintext = plaintext.upper()
    pl = len(plaintext)
    up = False
    ctlist = [""]*n
    k = 0
    for i in range(pl):
        if i % (n-1) == 0 and i != 0:
            if up:
                up = False
                k = 0
            else:
                up = True
                k = n-1
        if up:
            ctlist[k] += plaintext[i]
            k -= 1
        else:
            ctlist[k] += plaintext[i]
            k += 1
    # print(ctlist)
    return "".join(ctlist)


def decypher(cyphertext, n):
    #plaintext = ""
    cl = len(cyphertext)
    plaintext = ["" for _ in range(cl)]
    up = False
    ctlist = [[] for _ in range(n)]
    k = 0
    for i in range(cl):
        if i % (n-1) == 0 and i != 0:
            if up:
                up = False
                k = 0
            else:
                up = True
                k = n-1
        if up:
            ctlist[k].append(i)
            k -= 1
        else:
            ctlist[k].append(i)
            k += 1
    newlist = []
    for i in range(n):
        newlist += ctlist[i]
    # print(newlist)
    for i in range(cl):
        m = newlist[i]
        plaintext[m] = cyphertext[i]
    return "".join(plaintext)


cyphertext = cypher(plaintext, n)
print(cyphertext)
print(decypher(cyphertext, n))
