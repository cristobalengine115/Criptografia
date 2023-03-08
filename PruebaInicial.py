import fileinput
lines = []
for line in fileinput.input():
    lines.append(line)

def sumaNumeros(n):
    print(type(n))

sumaNumeros(lines)