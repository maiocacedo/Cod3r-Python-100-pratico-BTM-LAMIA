pessoas = ['Gui', 'Rebeca']
adjs = ['inteligente', 'sapeca']

for p in pessoas:
    for a in adjs:
        print(f'{p} é {a}')

for i in [1, 2, 3]:
    pass

for i in range(1, 11):
    if i % 2:
        continue
    print (i, end = ' ')
    
for i in range(1, 11):
    if i == 5:
        break
    print(i)
    