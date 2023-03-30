flag = str(input('Digite SIM para começar o programa: ')).upper()[0]
maiores18 = 0
qtdHomens = 0
mulheresMenos20 = 0
while flag != 'N':
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('É MASCULINO ou FEMININO: ')).upper()[0]
    flag = str(input('Quer continuar S/N: ')).upper()
    if idade > 18:
        maiores18+=1
    if sexo == 'M':
        qtdHomens+=1
    if sexo == 'F' and idade <20:
        mulheresMenos20+=1
print(f'A quantidade de pessoas maiores de 18 anos são {maiores18}!')
print(f'A quantidade de homens cadastrados foi {qtdHomens}!')
print(f'A quantidade de mulheres com menos de 20 anos é {mulheresMenos20}')