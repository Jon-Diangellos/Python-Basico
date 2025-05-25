#Converte um valor em reais para dólares usando uma taxa fixa de câmbio.

real = float(input('Me informe a quantidade que deseja converter: '))

dolar = real / 5.72

print('Você tem R${:.2f} que em dólar fica US${:.2f}'.format(real, dolar))
