numero_termos = int(input('Digite a quantidade de termos: '))
termo_um = 0
termo_dois = 1
termo_tres = termo_um + termo_dois
contador = 3
while contador <= numero_termos:
    termo_tres = termo_um + termo_dois
    termo_um = termo_dois
    termo_dois = termo_tres
    contador = contador + 1
    print(termo_tres, end=' → ')
print('fim')