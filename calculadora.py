print('-'*10,'CALCULADORA','-'*10)
condicaoParada = False
while not condicaoParada:
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite outro valor: '))
    choice = int(input('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    '''))
    if choice == 1:
        print('A soma de {} + {} = {}'.format(n1,n2,n1+n2))
    elif choice == 2:
        print('A multiplicação de {} x {} = {}'.format(n1,n2,n1*n2))
    elif choice == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}'.format(n1,n2,n1))
        else:
            print('Entre {} e {} o maior é {}'.format(n1,n2,n2))
    elif choice == 4:
        condicaoParada = False
    elif choice == 5:
        condicaoParada = True
print('Obrigado por utilizar nossos serviços!')