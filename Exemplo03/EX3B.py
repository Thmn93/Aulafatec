v = 0
frase = input("Digite a frase: ")
#frase = input("Digite a frase: ").upper // para não precisar repetir vogais maiusculas e minusculas
for vogal in "AEIOU":
    v = v + frase.count(vogal)

print(f"A frase têm {v} vogal(is).")