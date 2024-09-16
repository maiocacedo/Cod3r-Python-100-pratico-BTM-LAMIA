pessoas = ['Gilberto', 'Rebeca']
adjs = ['esperto', 'sapeca']

# Percorre as posições de pessoas e adjs e mostra cada pessoa com cada adjetivo.
for p in pessoas:
    for a in adjs:
        print(f'{p} é {a}')

# Percorre numeros entre 1 e 11 e mostra apenas os pares

for i in range(1, 11):
    if i % 2:
        continue
    print (i, end = ' ')