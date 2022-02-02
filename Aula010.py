resp = 'Ss'
cont = soma = maior = menor = media = 0
while resp in 'Ss':
    num = int(input('Digite um numero:'))
    resp = str(input('Quer continuar? S/N')).strip().upper()[0]
    cont = cont + 1
    soma = soma + num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print(f'Voçê digitou {cont} números ', end='')
print(f'A soma de todos é: {soma}', end='')
print(f'O maior é: {maior}', end='')
print(f'O menor é: {menor}')
print(f'A média de todos é: {media}')
