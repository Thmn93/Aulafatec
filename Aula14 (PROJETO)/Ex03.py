x = input("Insira o número: ")


def soma(args):
    total = 0
    for i in args:
        total += int(i)
    return total


print(f"Somado os números são: {soma(x)}")


def mult(args):
    total = 1
    for i in args:
        total *= int(i)
    return total


print(f"Multiplicados os números são: {mult(x)}")