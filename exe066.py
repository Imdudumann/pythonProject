n = 0
acumulador = 0
contador = 0
while True:
    n = int(input('Digite um valor ou [999] para sair: '))
    if n == 999:
        break
    acumulador +=n
    contador +=1
print(f'A soma de todos os valores digitados foi {acumulador}')
print(f'Você digitou {contador} números')