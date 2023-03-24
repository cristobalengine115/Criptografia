from email import message
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

def publicKey(message,n,e):
    cypher = (message * e)%n
    return cypher

def privateKey(cypher,d,n):
    decipher = (cypher*d)%n
    return  decipher

#Función main del programa
if __name__ == "__main__":
    lines = reveiveInput()
    oper = lines[0]
    a, b , A, B = lines[1], lines[2], lines[3], lines[4]
    message = lines[5]
    M = a*b - 1
    e = A*M + a
    d = B*M + b
    n = int(((e*d)-1)/M)
    if(oper=='E'):
        cypher = publicKey(message,n,e)
        print(cypher)
    if(oper=='D'):
        decipher = privateKey(message,d,n)
        print(decipher)
    

