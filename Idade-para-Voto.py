#O código solicita o nome e o ano de nascimento do usuário, 
#calcula sua idade em 2025 e informa se ele já pode votar (idade mínima: 16 anos).

nome=str(input('Qual seu nome ? '))
anodenasc=int(input('Em qual ano você nasceu?  '))

idade=(2025-anodenasc)

if idade >= 16:
    print(f'Seja bem Vindo {nome} Você ja tem {idade} e ja pode Votar!')

else:
    print(f'Me desculpe {nome} você ainda é muito novo para votar!')