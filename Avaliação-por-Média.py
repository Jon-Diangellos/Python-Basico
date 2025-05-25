#O programa calcula a média de duas notas e classifica o aluno como aprovado,
#em recuperação ou reprovado, conforme critérios definidos.

n1=float(input('Digite o valor da primeira nota: '))
n2=float(input('Digite o valor da segunda nota: '))

media=(n1+n2)/2

if (media>=7):
    print(f'Aprovado! {media}')

elif (media<7) and (media>=5.5):
    print(f'Recuperação! {media}')

else:
    print(f'Reprovado! {media}')
#