#Calcula o salário mensal com base na quantidade de dias trabalhados, 
# considerando 8 horas por dia e uma diária fixa de R$25.

dias=int(input('Informe a quantidade de dias que você trabalhou no mês: '))

valordia=8*25
sal=dias*valordia

print(f"você trabalhou {dias} dias este mês e seu salario é de R${sal:.2f}")