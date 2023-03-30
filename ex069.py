from random import randint


contador = 0
while True:
    minhaEscolha = int(input('Digite um número qualquer: '))
    escolhaComputador = randint(0,10)
    par_ou_impar = str(input('Você quer par ou impar? ')).upper().split()[0]
    soma = escolhaComputador + minhaEscolha
    if par_ou_impar == 'I':
        if (soma %2) == 1:
            print(f'Você escolheu {minhaEscolha} e o computador escolheu {escolhaComputador} ')
            print(f'A soma foi {soma} e você ganhou!')
            contador+=1
    elif par_ou_impar == 'P':
        if (soma%2) == 0:
            print(f'Você escolheu {minhaEscolha} e o computador escolheu {escolhaComputador}')
            print(f'A soma dos valores foi {soma} e você ganhou!')
            contador+=1
    if par_ou_impar == 'I':
        if (soma%2) == 0:
            print(f'Você escolheu {minhaEscolha} e o computador escolheu {escolhaComputador}')
            print(f'A soma foi {soma}, é par!')
            print('GAME OVER')
            print(f'Você ganhou {contador} vezes!')
            break
    if par_ou_impar == 'P':
        if (soma%2) == 1:
            print(f'Você escolheu {minhaEscolha} e o computador escolheu {escolhaComputador}')
            print(f'A soma foi {soma}, é impar!')
            print('GAME OVER')
            print(f'Você ganhou {contador} vezes!')
            break