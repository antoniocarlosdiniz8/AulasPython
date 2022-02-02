print(20*'=')
print('=====RODA-A-RODA=====')
print(20*'=')
palavra = 'GARÇOM'
dica = 'RESTAURANTE'
somapalavra = ' '
print(F'Dica: {dica}')
while True:
    tente = str(input('Tente uma letra:')).strip().upper()
    if tente in palavra:
        somapalavra = somapalavra + tente
        print(tente[0])
    else:
        tente = str(input('Tente Novamente:'))
    if somapalavra == palavra:
        break
print(f'{somapalavra} >> {palavra}')



