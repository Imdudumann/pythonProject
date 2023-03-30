from random import randint

computerChoice = randint(0,10)
escolha = False
while not escolha:
    myChoice = int(input('Digite um número para saber se acertou: '))
    if computerChoice == myChoice:
        escolha = True
print('Você acertou!')