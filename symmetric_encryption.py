import math
#key ="GOYI"
#cyphertext = "NELOIETECR 0OSE CAHADSLNHNTO0FAUONN O L.MME OA10R  FIN FA PE END0 MQNUO "

key = "VICTOR"
cyphertext = " L E CD0MEUAOA.LENA0RUFNEAIEEN  SNC  DMN T1F OI HLSMHOO0A NNNFOPTER0OQ O"

plaintext = "NO HE FALLADO. SIMPLEMENTE HE ENCONTRADO 10000 FORMAS QUE NO FUNCIONAN"


def cypher(key, plaintext):
    kl = len(key)
    ptl = len(plaintext)
    if ptl % kl != 0:
        plaintext += " "*(kl-(ptl % kl))

    size = int(len(plaintext)/kl)

    keyOrder = []
    for i in range(kl):
        keyOrder.append([key[i], i])
    keyOrder.sort(key=lambda x: x[0])

    pllist = []
    while len(plaintext) > 0:
        pllist.append(plaintext[0:kl])
        plaintext = plaintext[kl:]

    newlist = []

    for i in range(kl):
        text = ""
        for j in range(size):
            text += pllist[j][i]
        newlist.append(text)

    cypherlist = []
    for i in range(kl):
        cypherlist.append(newlist[keyOrder[i][1]])

    return "".join(cypherlist)


def decypher(key, cyphertext):
    kl = len(key)
    cl = len(cyphertext)

    j = int(cl/kl)

    chunks = []
    while len(cyphertext) > 0:
        chunks.append(cyphertext[0:j])
        cyphertext = cyphertext[j:]

    keyOrder = []
    for i in range(kl):
        keyOrder.append([key[i], i])
    keyOrder.sort(key=lambda x: x[0])

    orderedcyphertext = []
    for i in range(kl):
        index = keyOrder[i][1]
        orderedcyphertext.append([chunks[i], index])

    orderedcyphertext.sort(key=lambda x: x[1])

    message = ""
    for m in range(j):
        for n in range(kl):
            message += orderedcyphertext[n][0][m]
    return message


print(cypher("HOTEL", "LA DEMOCRACIA ES EL GOBIERNO DE LA GENTE, POR LA GENTE, PARA LA GENTE"))
print(decypher("HOTEL", "DR LI ATO ER ELMCSGREG, E  EEAE ED ERG,AG AOI ON E LNPLN CAEBOLNPATAAT"))
