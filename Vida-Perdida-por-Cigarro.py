#O programa calcula quantos dias, horas e minutos de vida uma pessoa pode ter 
# perdido com base na quantidade de cigarros fumados por dia e no tempo de hábito.

cigdia=int(input('Me fale quantos cigarros você fuma por dia: '))
cigAno=int(input('ha quanto tempo você fuma? '))

totalCig=cigdia*cigAno*365

tempdias=totalCig*10/1440

tempmin=tempdias*1440

temphoras=tempmin/60

print(f'Você ja perdeu um total de {tempdias:.0f} dias de vida que em horas dá {temphoras:.0f} e que em minutos dá {tempmin:.0f}')