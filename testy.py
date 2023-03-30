n1 = float(input('Digite um valor: '))
divide50 = int(n1//50)
resto = int(n1%50)
divide20 = resto//20
divide10 = resto//10
if resto == 0:
    print(f'vai ter {divide50} de 50')
else:
    if resto != 0:
        print(f'vai ter {divide50} de 50')
        print(f'vai ter {divide20} de 20')
        print(int(n1-(divide50*50+divide20*20)))
    else:
        if (int(n1-(divide50*50+divide20*20))) >10:
            print(f'vai ter {divide50} de 50')
            print(f'vai ter {divide20} de 20')
            print(f' vai ter {divide10} de 10')