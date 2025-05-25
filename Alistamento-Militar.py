#O programa calcula a idade do usuário com base no ano de nascimento 
#e informa se ele já pode se alistar, se ainda falta tempo ou se passou do prazo para o alistamento.

anodenasc=int(input('Em que ano você nasceu? '))
idade=(2025-anodenasc)

if idade==18:
  print('Você ja pode ir se alistar')
elif idade<18:
  print(f'Você ainda não pode se alistar, faltam {18-idade} anos')
else:
  print(f'Você Ja passou da idade de se alistar, ja foram {idade-18} anos')