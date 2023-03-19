from cgitb import text
import fileinput
from operator import sub
from pydoc import plain
from turtle import right
from xml.etree.ElementTree import QName

S0_Box = [[1,0,3,2],
        [3,2,1,0],
        [0,2,1,3],
        [3,1,3,2]]

S1_Box = [[0,1,2,3],
        [2,0,1,3],
        [3,0,1,0],
        [2,1,0,3]]
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


def SubKeysGen(key):
    k1 = key[0] + key[6] + key[8] + key[3] + key[7] + key[2] + key[9] + key[5]
    k2 = key[7] + key[2] + key[5] + key[4] + key[9] + key[1] + key[8] + key[0]
    return k1, k2

def InitialPermutation(plainText):
    p = plainText[1] +  plainText[5] +  plainText[2] +  plainText[0] +  plainText[3] +  plainText[7] +  plainText[4] +  plainText[6]
    return p

def FeistelOperation(subkey, Text):
    rightHalf = Text[4:8]
    leftHalf = Text[0:5]
    expanded = rightHalf[3] + rightHalf[0] + rightHalf[1] + rightHalf[2] + rightHalf[1] + rightHalf[2] + rightHalf[3] + rightHalf[0]
    coordsBin = [(ord(a) ^ ord(b)) for a, b in zip(expanded, subkey)]
    coord1 = int(str(coordsBin[0]) + str(coordsBin[3]),2)
    coord2 = int(str(coordsBin[1]) + str(coordsBin[2]),2)
    coord3 = int(str(coordsBin[4]) + str(coordsBin[7]),2)
    coord4 = int(str(coordsBin[5]) + str(coordsBin[6]),2)
    s0 = S0_Box[coord1][coord2]
    s1 = S1_Box[coord3][coord4]
    s0 = bin(s0)[2:].zfill(2).replace("0b", "")
    s1 = bin(s1)[2:].zfill(2).replace("0b", "")
    FeistelText = s0+s1
    FeistelText = FeistelText[1]+FeistelText[3]+FeistelText[2]+FeistelText[0]
    FeistelText = [(ord(a) ^ ord(b)) for a, b in zip(FeistelText, leftHalf)]
    FeistelText = ''.join(map(str,FeistelText))
    FeistelText = FeistelText + rightHalf
    return FeistelText

def switchRightLeft(text):
    text = text[4:8] + text[0:4]
    return text

def inversePermutation(text):
    inverse = text[3] + text[0] + text[2] + text[4] + text[6] + text[1] + text[7] + text[5]
    return inverse
#Función main del programa
if __name__ == "__main__":
    lines = reveiveInput()
    oper = lines[0]
    plainText = lines[1]
    key = lines[2]
    if(oper == 'E'):
        plainText = '01010101'
        key = '0000011111'
        plainText = InitialPermutation(plainText)
        k1, k2 = SubKeysGen(key)
        feistel1 = FeistelOperation(k1, plainText)
        feistel1 = switchRightLeft(feistel1)
        feistel2 = FeistelOperation(k2, feistel1)
        cipherText = inversePermutation(feistel2)
        print(cipherText)
    if(oper == 'D'):
        plainText = '11110000'
        key = '0000000000'
        plainText = InitialPermutation(plainText)
        k1, k2 = SubKeysGen(key)
        feistel1 = FeistelOperation(k2, plainText)
        feistel1 = switchRightLeft(feistel1)
        feistel2 = FeistelOperation(k1, feistel1)
        cipherText = inversePermutation(feistel2)
        print(cipherText)