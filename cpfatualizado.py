cpf = [4, 5, 6, 1, 2, 2, 1, 3, 8, 7, 6]

def executar():
    cpf_menor = cpf[:9] #pega da primeira até a oitava posição
    resultado = []
    resultado2 = []

    #para cada numero contido no cpf 
    contador = 10
    for num in cpf_menor:
        resultado.append(num * contador)
        contador -= 1
       
    soma = sum(resultado)
    resto = soma % 11

    if resto < 2:
        digito_ver = 0
    elif resto >= 2:
        digito_ver = (11 - resto)

    cpf_menor.append(digito_ver)
    
    contador = 11
    for num in cpf_menor:
        resultado2.append(num * contador)
        contador -= 1
    
    soma2 = sum(resultado2)
    resto2 = soma2 % 11

    if resto2 < 2:
        digito_ver2 = 0
    elif resto2 >= 2:
        digito_ver2 = (11 - resto2)

    cpf_menor.append(digito_ver2)  
    
    if cpf_menor == cpf:
        print('Seu CPF é válido')
    else:
        print("Seu CPF é inválido")

executar()