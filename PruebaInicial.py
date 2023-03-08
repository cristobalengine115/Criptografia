import fileinput
lines = []
for line in fileinput.input():
    lines.append(line)

def clearLines(lines):
    newLines = [x[:-1] for x in lines]
    return lines


def sumaNumeros(n):
    print(n)

numbers = clearLines(lines)
sumaNumeros(numbers)