import fileinput
lines = []
for line in fileinput.input():
    lines.append(line)

def sumaNumeros(lines):
    print(sum(lines))

sumaNumeros()