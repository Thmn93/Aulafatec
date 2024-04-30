idade_por_sobrenome = {}
#preenche o dicionário:\/

for _ in range (3):
    sobrenome = input("Digite o Sobrenome da pessoa:")
    idade = int(input("Digite a idade da pessoa:"))
    idade_por_sobrenome[sobrenome] = idade

#Econtra o sobrenome da pessoa mais velha: \/
sobrenome_mais_velho = max(idade_por_sobrenome, key=idade_por_sobrenome.get)

#Exibe o resultado
print(f"O Sobrenome da pessoa mais mais velha é: {sobrenome_mais_velho}")