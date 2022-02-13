import re

def remove_char(cnpj:str) -> str:
    return re.sub(r'[^0-9]', '', cnpj)

def cnpj_sem_digito(cnpj):
    return cnpj[:12]

def calc_d1(cnpj):
    cnpj_p1 = cnpj[:4]
    cnpj_p2 = cnpj[4:12]
    total_p1 = 0
    total_p2 = 0

    for cont, mult in enumerate(range(len(cnpj_p1)+1, 1, -1)):
        total_p1 += (mult * int(cnpj_p1[cont]))

    for cont, mult in enumerate(range(len(cnpj_p2)+1, 1, -1)):
        total_p2 += (mult * int(cnpj_p2[cont]))

    calc = 11 - ((total_p1 + total_p2) % 11)

    return 0 if calc > 9 else calc

def calc_d2(cnpj):
    cnpj_p1 = cnpj[:5]
    cnpj_p2 = cnpj[5:12]+f'{calc_d1(remove_char(cnpj))}'
    total_p1 = 0
    total_p2 = 0

    for cont, mult in enumerate(range(len(cnpj_p1)+1, 1, -1)):
        total_p1 += (mult * int(cnpj_p1[cont]))

    for cont, mult in enumerate(range(len(cnpj_p2)+1, 1, -1)):
        total_p2 += (mult * int(cnpj_p2[cont]))

    calc = 11 - ((total_p1 + total_p2) % 11)

    return 0 if calc > 9 else calc

def gerador_cnpj(cnpj_l):
    base_cnpj = cnpj_sem_digito(cnpj_l)
    digito1 = calc_d1(cnpj_l)
    digito2 = calc_d2(cnpj_l)
    return base_cnpj + '' + str(digito1) + '' + str(digito2)

def cnpj_valido(cnpj):
    cnpj_limpo = remove_char(cnpj)
    cnjp_valido = gerador_cnpj(cnpj_limpo)
    return cnjp_valido == cnpj_limpo

cnpj = ''
while True:
    cnpj = input('Digite o cnpj que deseja testar (Digite 0 pra sair):')
    if cnpj != '0':
        if cnpj_valido(cnpj):
            print(f'O CNPJ {cnpj} eh valido!!!')
        else:
            print('Esse CNPJ nao eh valido!!!')
    else:
        break




