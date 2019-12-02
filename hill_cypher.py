import math

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def gen_key_matrix(key):
    key = key.upper()
    n = int(math.sqrt(len(key)))
    cypher_matrix = []
    index = 0
    for i in range(n):
        row = []
        for j in range(n):
            k = alphabet.index(key[index])
            row.append(k)
            index += 1
        cypher_matrix.append(row)
    return cypher_matrix


def cypher(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.upper()
    key = key.upper()
    key_matrix = gen_key_matrix(key)
    n = int(math.sqrt(len(key)))

    # completar con la letra U o Z
    if len(plaintext) % n != 0:
        plaintext = plaintext + "Z"*(n-(len(plaintext) % n))

    index = 0
    cyphertext = ""
    for u in range(int(len(plaintext)/n)):
        vector = []
        for v in range(n):
            k = alphabet.index(plaintext[index])
            # vector.append(hillAphabet[k])
            vector.append(k)
            index += 1

        for i in range(n):
            s = 0
            for j in range(n):
                s += key_matrix[i][j]*vector[j]
            cyphertext += alphabet[s % 26]
    return cyphertext


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    else:
        s = 0
        i = 0
        for j in range(n):
            matrixB = [matrix[i].copy() for i in range(n)]
            matrixB.pop(i)
            for k in range(n-1):
                matrixB[k].pop(j)
            s += matrix[i][j]*(int(math.pow(-1, i+j+2)))*determinant(matrixB)
        return s


def adj(matrixA):
    n = len(matrixA)

    for i in range(n):
        for j in range(n):
            if j > i:
                a = matrixA[i][j]
                b = matrixA[j][i]
                matrixA[i][j] = b
                matrixA[j][i] = a

    adjugate = []
    for i in range(n):
        row = []
        for j in range(n):
            c = int(math.pow(-1, i+j+2))
            matrixB = [matrixA[i].copy() for i in range(n)]
            matrixB.pop(i)
            for k in range(n-1):
                matrixB[k].pop(j)

            row.append((c*determinant(matrixB)) % 26)
        adjugate.append(row)

    return adjugate


def decypher(cyphertext, key):
    key = key.upper()
    key_matrix = gen_key_matrix(key)
    adjMatrix = adj(key_matrix)
    n = int(math.sqrt(len(key)))
    d = determinant(key_matrix)
    x = 1

    d = d % 26
    for i in range(1, 26):
        if ((d * i) % 26 == 1):
            x = i
            break

    for i in range(n):
        for j in range(n):
            adjMatrix[i][j] = (adjMatrix[i][j]*x) % 26

    plaintext = ""

    index = 0
    for u in range(int(len(cyphertext)/n)):
        vector = []
        for v in range(n):
            k = alphabet.index(cyphertext[index])
            # vector.append(hillAphabet[k])
            vector.append(k)
            index += 1
        for i in range(n):
            s = 0
            for j in range(n):
                s += adjMatrix[i][j]*vector[j]
            #g = hillAphabet[s%26]

            plaintext += alphabet[s % 26]
    return plaintext


print(cypher("shortexample", "hill"))
print(decypher("APADJTFTWLFJ", "hill"))
