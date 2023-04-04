resposta = "SIM"
while resposta == "SIM":
    nivel = input(f'Digite o nível de acesso: ').upper()
    if nivel == "ADM" or nivel == "USR":
        genero = input(f'Digite seu genero: ').upper()
        if nivel == "ADM":
            if genero == "M":
                print(f'Olá administrador!')
            elif genero == "F":
                print(f'Olá administradora!')
            else:
                print(f'informe seu genero.')

        if nivel == "USR":
            if genero == "M":
                print(f'Olá Usuário!')
            elif genero == "F":
                print(f'Olá Usuária!')
            else:
                print(f'informe seu genero.')

    elif nivel == "GUEST":
        print(f'Olá Visitante!')

    else:
        print(f'Olá Desconhecido(a)!')

    resposta = input("Digite SIM para continuar: ").upper()