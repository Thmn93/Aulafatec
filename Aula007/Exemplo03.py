soma = 0
idade = 100
qtd = 0
while idade != 0:
    idade = int(input(f"Entre com a idade {qtd+1}:  "))
    if idade !=0:
        soma = soma + idade
        qtd = qtd + 1
media = soma / 5
print(f"A média das idades é {round(media)}) anos.")