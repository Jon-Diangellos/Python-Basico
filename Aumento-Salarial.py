#O programa calcula o novo salário após aplicar um aumento de 15% sobre o valor informado pelo usuário.

sal=float(input('Me informe seu salario para que eu possa acrescentar os 15% de aumento: '))

aumento=sal+(sal*0.15)


print(f'Seu salario era de: {sal:.2f} e seu novo salario é de: {aumento:.2f}')