#O programa recebe o salário do trabalhador e o valor da prestação do empréstimo, 
#e verifica se a prestação ultrapassa 20% do salário, decidindo se o empréstimo é concedido ou não.

salario = float(input("Digite o salário do trabalhador: "))
prestacao = float(input("Digite o valor da prestação do empréstimo: "))

if prestacao > 0.20 * salario:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")