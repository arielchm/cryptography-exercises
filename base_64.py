message = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure."
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def cypher(message):
    message_length = len(message)
    bin_chain = ""
    for c in message:
        bin_value = bin(ord(c))[2:]
        if len(bin_value) < 8:
            bin_value = '0'*(8-len(bin_value))+bin_value
            bin_chain += bin_value

    chain_lenth = len(bin_chain)
    bin_chain += "0"*(6-chain_lenth % 6)
    cyphertext = ""

    for i in range(0, len(bin_chain), 6):
        index = int(bin_chain[i:i+6], 2)
        letter = alphabet[index]
        cyphertext += letter

    return cyphertext


def decypher(secret):
    message = ""
    bin_chain = ""
    for c in secret:
        val = alphabet.index(c)
        bin_value = bin(val)[2:]
        if len(bin_value) < 6:
            bin_value = '0'*(6-len(bin_value))+bin_value
        bin_chain += bin_value
        # print(val)
        # print(bin_value)
    remainder = len(bin_chain) % 8
    bin_chain = bin_chain[:-remainder]

    for i in range(0, len(bin_chain), 8):
        index = int(bin_chain[i:i+8], 2)
        message += chr(index)

    return message


print(cypher(message))
secret = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4"

print(decypher(secret))
