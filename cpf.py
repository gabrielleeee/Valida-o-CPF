def executar():

    d1 = int(input("Digite o 1º número: "))
    d2 = int(input("Digite o 2º número: "))
    d3 = int(input("Digite o 3º número: "))
    d4 = int(input("Digite o 4º número: "))
    d5 = int(input("Digite o 5º número: "))
    d6 = int(input("Digite o 6º número: "))
    d7 = int(input("Digite o 7º número: "))
    d8 = int(input("Digite o 8º número: "))
    d9 = int(input("Digite o 9º número: "))
    d10 = int(input("Digite o 10º número: "))
    d11 = int(input("Digite o 11º número: "))

    a1 = d1
    a2 = d2
    a3 = d3
    a4 = d4
    a5 = d5
    a6 = d6
    a7 = d7
    a8 = d8
    a9 = d9
    a10 = d10
    a11 = d10

    c10 = d10
    c11 = d11

    d1 = d1 * 10
    d2 = d2 * 9
    d3 = d3 * 8
    d4 = d4 * 7
    d5 = d5 * 6
    d6 = d6 * 5
    d7 = d7 * 4
    d8 = d8 * 3
    d9 = d9 * 2
    
    soma = (d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9)
    resto = (soma % 11)

    if soma % 11 == 1:
        d10 = 0
    elif resto > 1:
        d10 = 11 - resto
    else:
        print('erro!')
    
    a1 = a1 * 11
    a2 = a2 * 10
    a3 = a3 * 9
    a4 = a4 * 8
    a5 = a5 * 7
    a6 = a6 * 6
    a7 = a7 * 5
    a8 = a8 * 4
    a9 = a9 * 3
    a10 = d10 * 2

    soma2 = (a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10)
    resto2 = (soma2 % 11)

    if soma2 % 11 == 1:
        d11 = 0
    elif resto2 > 1:
        d11 = 11 - resto2
    else:
        print('erro!')

    if d10 == c10 and d11 == c11:
        print('Seu CPF é válido!')
    else:
        print('Seu CPF é inválido!')

executar()