from random import randint
from valida_data import valida_data


def valida_cpf(cpf):
    cpf = input("Digite o cpf no formato XXX.XXX.XXX-XX: ")
    # Remover caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcular o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Verificar o primeiro dígito verificador
    if digito1 != int(cpf[9]):
        return False

    # Calcular o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # Verificar o segundo dígito verificador
    if digito2 != int(cpf[10]):
        return False

    return True

def menu():
    print('''
    Menu de Opções: 

    1 - Cadastrar 
    2 - Exibir Frase
    3 - Sair
    ''')
def cadastrar():
    nome = input("Digite seu nome: ")
    usuario.append(nome)
    nome = input("Digite seu sobrenome: ")
    usuario.append(nome)
    valida_cpf(cpf=True)
    valida_data()
def frase_motivacional():
    a = "A persistência realiza o impossível"
    b = "Seus sonhos não precisam de plateia, eles só precisam de você"
    c = "A persistência é o caminho do êxito"
    d = "No meio da dificuldade encontra-se a oportunidade"
    e = randint(1,4)
    if e == 1:
        print(a)
    elif e == 2:
        print(b)
    elif e == 3:
        print(c)
    elif e == 4:
        print(d)
    return


x = 0
nome = "x"
usuario = []
renda = 0

while x != -1:
    menu()
    x = int(input("Selecione uma opção: "))
    if x == 1:
        cadastrar()

    if x == 2:
        frase_motivacional()

    if x == 3:
        print("Bye bye!")
        x = -1