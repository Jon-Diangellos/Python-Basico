#O programa solicita um número positivo do usuário e exibe sua raiz quadrada. 
#Se o número for menor ou igual a zero, exibe uma mensagem de erro.

n1=int(input('Digite um numero: '))
import math

if n1<=0:
    print('Numero Invalido!')

else:
    n1>0
    print(f'A raiz quadrada de {n1} é {math.sqrt(n1)}')