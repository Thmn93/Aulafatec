#Slice de strings: 3 parâmetros:
#1 - início
#2 - limite superior (ele pegará até o n-1)
#3 - tamanho do passo (se deixar em branco, passo igual a 1)
frase="Seja um profissional Python"
print(frase[0:15:1])
print(frase[0:15:2])
print(frase[15:0:-1])
print(frase[15::-1])
print(frase[::-1])

print("Seja" in frase)