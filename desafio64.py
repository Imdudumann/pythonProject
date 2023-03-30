contador = 0
acumulador = 0
flag = int(input('Digite 1 para começar e 999 para sair: '))
while flag != 999:
    num = int(input('Digite os números que deseja somar: '))
    acumulador += num
    contador +=1
    flag = int(input('Digite 999 para sair: '))
print('A soma de todos os valores foi {}'.format(acumulador))
print('Você digitou {} valores'.format(contador))