#O programa calcula uma recompensa financeira baseada na quantidade de horas de atividade física praticadas pelo usuário, 
# aplicando diferentes taxas conforme faixas de horas.

qhoras=int(input('quantas horas de atividade fisica voce praticou? '))

if (qhoras<=10):
  valor=2*qhoras*0.05
  print(f'parabens esse mes voce conseguiu R$: {valor:.2f}')
elif (qhoras>=20) and (qhoras<=20):
  valor=5*qhoras*0.05
  print(f'parabens esse mes voce conseguiu R$: {valor:.2f}')

else:
  valor=10*qhoras*0.05
  print(f'parabens esse mes voce conseguiu R$: {valor:.2f}')