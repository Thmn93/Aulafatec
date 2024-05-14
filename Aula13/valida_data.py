from datetime import datetime


def valida_data():
    str_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    dia = str_nascimento[0:2]
    mes = str_nascimento[3:5]
    ano = str_nascimento[6:10]
    if not dia.isnumeric() or not mes.isnumeric() or not ano.isnumeric():
        return False  # pegou algum caractere que não é número
    elif len(dia) != 2 or len(mes) != 2 or len(ano) != 4:
        return False  # não digitou a data corretamente
    else:
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

    if mes < 1 or mes > 12:
        return False  # mês inválido
    if ano < 1900:
        return False  # ano inválido

    if dia < 1:
        return False  # dia inválido menor que 1
    elif mes == 2 and dia > 29 - int(ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
        return False  # dia inválido para fevereiro
    elif mes % 2 == 0 and dia > 30 + int(mes > 7):
        return False  # dia inválido para mês par
    elif mes % 2 != 0 and dia > 31 - int(mes > 7):
        return False  # dia inválido para mês ímpar

    data_atual = datetime.now()
    data_nascimento = datetime.strptime(str_nascimento, '%d/%m/%Y')
    delta_data = data_atual - data_nascimento
    idade = delta_data.days // 365.25
    if idade >= 18:
        print('Usuário é maior de idade, pode ser cadastrado')
    else:
        print('Usuário é menor de idade, não pode ser cadastrado')

    return True