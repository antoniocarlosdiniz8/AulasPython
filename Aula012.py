cont = soma = tot1000 = nomemenor =menor = cont1000 = 0
nontot1000 = ' '
while True:
    produto = str(input('Digite o produto:'))
    preco = float(input('Digite o preço: R$'))
    cont = cont + 1
    soma = soma + preco
    resp = ' '
    if preco > 1000:
        cont1000 = cont1000 + 1
        nontot1000 = produto
        tot1000 = preco
    if cont == 1 or preco < menor:
        menor = preco
        nomemenor = produto
    #else:
        #if preco < menor:
            #menor = preco
            #nomemenor = produto
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N')).strip().upper()[0]
    if resp in 'N':
        break
print(f'A soma dos produtos é: {soma}')
print(f'Temos {cont1000} maiores que 1000 R$ {nontot1000}  e custa: {tot1000:.2f}')
print(f'O produto mais barato {nomemenor} e custa: {menor}')
