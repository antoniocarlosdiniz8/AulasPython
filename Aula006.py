rota = []
nrota = str(input('Digite o numero da rota:'))
periodo = str(input('Digite o periodo do dia'))
while True:
    clientes = str(input('Digite um cliente:'))
    if clientes not in rota:
        rota.append(clientes)
    else:
        print('Voçê já digitou esse cliente:')
    resp = str(input('Quer continuar: S/N')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'ROTA {nrota.zfill(2)}', end=' ')
print(f'{periodo.upper()}')

for i, v in enumerate(rota):
    print(f'{i+1} {v.upper()}')
