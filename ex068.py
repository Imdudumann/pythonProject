numerotabu = int(input('Digite um valor para saber sua tabuada: '))
while True:
    for x in range(0,11):
        print(f'{numerotabu}x{x} = {numerotabu*x}')
    numerotabu = int(input('Digite o valor para saber sua tabuada: '))
    if numerotabu == 999:
        break