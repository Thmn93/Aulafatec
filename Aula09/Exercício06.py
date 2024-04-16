#pegar no Git para treinar

from random import randint
resultados = [0]*13
freq = [0]*13
print(resultados)
for _ in range  (30000):
    jogada1 = randint(1,6)
    jogada2 = randint(1,6)
    soma = jogada1+jogada2
    resultados[soma] = resultados[soma] + 1

for i in range  (1,13):
    print(f"{jogada1} - {resultados[i]} - {freq[jogada2]:6.2f}%")
