n1 = int(input('Digite quantos termos vão ter a sua sequencia de fibonacci: '))
termo1 = 0
termo2 = 1
termo3 = termo1+termo2
contador = 3
while contador <=n1:
    termo3 = termo1+termo2
    termo1 = termo2
    termo2 = termo3
    contador +=1
    print(termo3,'→',end=' ')
print('fim')