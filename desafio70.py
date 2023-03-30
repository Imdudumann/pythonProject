print(f'*'*30)
print('       MERCADÃO DEV')
print(f'*'*30)
listra_preço_produto = []
lista_produtosMais1000 = []
menor = contador = 0
flag = str(input('Digite SIM para começar e NÃO para sair: ')).upper().split()[0]
while flag != 'N':
    nome_produto = str(input('Digite o nome do produto: '))
    preço_produto = float(input('Digite o preço do produto: '))
    contador+=1
    if contador ==1:
        menor = preço_produto
    else:
        if preço_produto < menor:
            menor = preço_produto
    listra_preço_produto.append(preço_produto)
    if preço_produto > 1000:
        lista_produtosMais1000.append(preço_produto)
    flag = str(input('Quer continuar? [S/N]: ')).upper()[0]
print(f'O total gasto na compra foi {sum(listra_preço_produto)}R$ ')
print(f'{len(lista_produtosMais1000)} produtos custaram mais de 1000R$')
print(f'O menor preço foi {menor}')