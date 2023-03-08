import fileinput
from pydoc import plain


#Función que recibe las valores de entrada del programa para ejecutar los test cases.
def reveiveInput():
    lines = []
    newLines = []
    for line in fileinput.input():
        lines.append(line)
    #Quitando los salto de linea de las entradas
    for sub in lines:
        newLines.append(sub.replace("\n", ""))
    return newLines

#Función que realiza el algoritmo KSA para realizar una permUtación de valores de una matriz S.
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

#Función que realiza el algorirmo PRGA, el cual genera el keystream para cifrar el texto plano
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

#Función main del programa
if __name__ == "__main__":
    #Iniciando listas convenientes para la ejecución del programa
    cypherText = []
    keyStreamHex = []
    cypherTextDec = []
    cypherTextHex = []

    #Recibiendo entradas de Alphagrader (la key y el texto plano)
    lines = reveiveInput()
    key = lines[0]
    plainText = lines[1]

    #Obteniendo matriz S
    S = KSA(key)

    #Obteniendo keystream con valor expresado en decimal.
    keyStreamDec = PRGA (S, len(plainText))

    #En este ciclo se obtiene el valor del keystream en hexadecimal y en mayusculas.
    for i in range(0, len(keyStreamDec)):
        keyStreamHex.append(format(keyStreamDec[i], 'x'))
        keyStream = ''.join(keyStreamHex).upper()
    
    #Obteniendo valor en ascii del texto plano
    plainText = [ord(c) for c in plainText]
    
    #Cifrando texto plano haciendo operaciones XOR
    for i in range(0, len(plainText)):
        cypherTextDec.append(plainText[i] ^ keyStreamDec[i])

    #Expresando el texto cifrado en hexadecimal
    for i in range(0, len(cypherTextDec)):
        cypherTextHex.append(hex(cypherTextDec[i])[2:].zfill(2))
        cypherText = ''.join(cypherTextHex).upper()
    
    #Imprimiendo texto cifrado final
    print(cypherText)