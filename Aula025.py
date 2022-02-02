'''entregas = ('gdm', 'bendsteel', 'lg', 'elgin', 'tigre', 'recofarma')

for i, e in enumerate(entregas):
    print(f'{i+1}. {e.upper()}')'''

produto = ('café', 'arroz', 'macarrão', 'cheiro-verde', 'mastruz')
preço = (5.50, 4.00, 3.50, 2.50, 5.00)

for material, preço in zip(produto, preço):
    print(f'{material}........{preço}')







