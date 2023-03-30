flag = int(input('Digite 1 para começar e 999 para sair: '))
contador = 0
lista = []
while flag != 999:
    myNumbers = int(input('Digite os valores: '))
    lista.append(myNumbers)
    flag = int(input('Digite 1 para continuar e 999 para sair:  '))
    contador +=1
tamanho_lista = len(lista)
soma_lista = sum(lista)
media_lista = soma_lista//tamanho_lista
print('A média dos valores digitados foi {}'.format(media_lista), end=' ' )
print('O maior número da lista é {}'.format(max(lista)),end=' ')
print('O menor número da lista foi {}'.format(min(lista)),end=' ')