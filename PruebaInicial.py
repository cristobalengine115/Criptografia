import fileinput
lines = []
for line in fileinput.input():
    lines.append(line)

def sumaNumeros(n):
    print(sum(n))

sumaNumeros(lines)