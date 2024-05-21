def primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
def primeiros(x):
    primos = []
    numero = 0
    while len(primos) < x:
        if primo(numero):
            primos.append(numero)
        numero += 1
    elementos = len(primos)
    print(f"Existem {elementos} elementos na lista")
    return primos


print("Verificar Numero Primo")
verif = int(input("Digite um número para verificação: "))
if primo(verif):
    print(f"{verif} é número primo")
else:
    print(f"{verif} não é número primo")


Y = 44
atributo = Y*2+5

print("Verificar número primo")
x = int(input("Digite um valor: "))
print(primeiros(x))
print("Final do ra 44*2+5")
lista = primeiros(atributo)
print(lista)
print("Soma da lista é: ")
lista_quantidade = sum(lista)
print(f"A soma dos números da lista anterior é igual a {lista_quantidade}")

