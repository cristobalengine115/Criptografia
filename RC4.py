import fileinput
from pydoc import plain

def reveiveInput():
    lines = []
    for line in fileinput.input():
        lines.append(line)
    return lines


def KSA(key):
    S = []
    keyLength = len(key)
    #Iniciando arreglo de bytes
    for i in range(0, 256):
        S.append(i)
    #Iniciando permutaciones del vector S
    j = 0
    for i in range(0, 256):
        asciiValue = [ord(c) for c in key[i % keyLength]]
        j = (j + S[i] + asciiValue[0]) % 256
        flag = S[i]
        S[i] = S[j]
        S[j] = flag
    return S


def PRGA(S, textLenght):
    i, j, n = [0, 0, 0]
    keyStream = []
    while (n < textLenght):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        flag = S[i]
        S[i] = S[j]
        S[j] = flag
        k = S[(S[i] + S[j]) % 256]
        keyStream.append(k)
        n += 1
    return keyStream

if __name__ == "__main__":
    cypherText = []
    keyStreamHex = []
    cypherTextDec = []
    cypherTextHex = []
    lines = reveiveInput()
    key = lines[0]
    S = KSA(key)
    plainText = lines[1]
    print(key, plainText)
    keyStreamDec = PRGA (S, len(plainText))
    for i in range(0, len(keyStreamDec)):
        keyStreamHex.append(format(keyStreamDec[i], 'x'))
        keyStream = ''.join(keyStreamHex).upper()
    plainText = [ord(c) for c in plainText]
    
    for i in range(0, len(plainText)):
        cypherTextDec.append(plainText[i] ^ keyStreamDec[i])
    for i in range(0, len(cypherTextDec)):
        cypherTextHex.append(hex(cypherTextDec[i])[2:].zfill(2))
        cypherText = ''.join(cypherTextHex).upper()
    print(cypherText)