while True:
    valor_saque = float(input('Digite um valor: $ '))
    notas50 = int(valor_saque//50)
    notas20 = int(valor_saque//20)
    resto_divisão_50 = int(valor_saque%50)
    resto_divisão_20 = int(resto_divisão_50%20)
    resto_divisão_10 = int(resto_divisão_20%10)
    if notas50 != 0:
        print(f'Vão ser {notas50} de 50$')
        print(f'vão ser {resto_divisão_50//20} de 20$')
        print(f'Vão ser {resto_divisão_20//10} de 10$')
        print(f'Vão ser {resto_divisão_10} de 1$')
