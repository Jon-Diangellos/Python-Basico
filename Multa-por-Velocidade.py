#O programa lê a velocidade do carro e calcula a multa se a velocidade ultrapassar 80 km/h, 
#informando o valor da multa ou que não houve penalidade.

vel=int(input('Qual a velocidade do carro? '))

if (vel>80):
    multa=(vel-80)*5
    print(f'Voce foi multado em R$: {multa:.2f}')

else:
    print('voce nao foi multado!')
