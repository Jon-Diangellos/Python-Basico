#O programa recebe dois números do usuário e informa qual deles é o maior.

n1 = int(input('Me fale um número: '))
n2 = int(input('Me fale outro número e eu direi qual é o maior: '))

if n1 > n2:
    print(f'O número maior é {n1}')
elif n2 > n1:
    print(f'O número maior é {n2}')
else:
    print('Os dois números são iguais.')
