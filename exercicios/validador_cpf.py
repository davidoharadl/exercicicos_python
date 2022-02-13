# transformar em list com inteiro retirando os . e -
def text_for_list_int(text:str) -> list:
    """
    :todo tratar outros tipos de caracteres
    """
    list_clear = []
    for digit in text:
        # print(digit)
        if (digit == '.' or digit == '-'):
            continue
        else:
            list_clear.append(int(digit))
    return list_clear

# digitos iguais tb sao invalidos
def validate_digits_diferent(lista:list) -> bool:
    status = False
    for pos, digit in enumerate(lista):
        if (len(lista)-1) != pos:
            if digit != lista[pos+1]:
                status = True
    return status

# validar se temos 11 digitos
def validate_qnt_digitos(lista:list) -> bool:
    return len(lista) == 11

# dividir em 3 partes(cpf 9 primeiros, cpf 1digito e cpf 2 digito)
def cpf_part_calc9(lista:list) -> list:
    return lista[:9]

def cpf_part_calc10(lista:list) -> list:
    return lista[:10]

def cpf_part_digit1(lista:list) -> list:
    return lista[-2]

def cpf_part_digit2(lista:list) -> list:
    return lista[-1]

# calculo dos 9 digitos validate 1
def calc_9digits1(lista:list) -> int:
    new_lista = cpf_part_calc9(lista)
    lista_mult = []
    result = 0
    for pos, mult in enumerate(range(10, 1, -1)):
        lista_mult.append(mult * new_lista[pos])

    for digit in lista_mult:
        result += digit
    return result

# calculo dos 9 digitos validate 2
def calc_9digits2(lista:list) -> int:
    new_lista = cpf_part_calc10(lista)
    lista_mult = []
    result = 0
    for pos, mult in enumerate(range(11, 1, -1)):
        lista_mult.append(mult * new_lista[pos])

    for digit in lista_mult:
        result += digit
    return result

# validacao 1
def validate_digit1(lista:list) -> bool:
    calc = (calc_9digits1(lista) * 10) % 11
    return calc == cpf_part_digit1(lista)

def validate_digit2(lista:list) -> bool:
    calc = (calc_9digits2(lista) * 10) % 11
    return calc == cpf_part_digit2(lista)

while True:
    cpf = input('Digite o cpf que deseja validar [0 -> Stop] :  ')
    if cpf != '0':
        lista_cpf = text_for_list_int(cpf)

        if(validate_qnt_digitos(lista_cpf) and validate_digits_diferent(lista_cpf)):
            if validate_digit1(lista_cpf) and validate_digit2(lista_cpf):
                print("###################")
                print("#   CPF VALIDO    #")
                print("###################")
            else:
                print("######################")
                print("#    CPF N VALIDO    #")
                print("######################")
        else:
            print("######################")
            print("#    CPF N VALIDO    #")
            print("######################")
    else:
        break
