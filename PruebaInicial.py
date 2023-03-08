import fileinput
lines = []
for line in fileinput.input():
    lines.append(line)

def clearLines(lines):
    newLines = [x[:-1] for x in lines]
    numbers = [eval(i) for i in newLines]
    return numbers


def sumaNumeros(n):
    print(sum(n))

numbers = clearLines(lines)
sumaNumeros(numbers)