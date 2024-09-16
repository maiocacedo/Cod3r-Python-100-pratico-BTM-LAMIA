total = 0
qtde = 0
num = 0


while num != -1:
    num = float(input('informe um número ou -1 para sair: '))
    if num != -1:
        qtde += 1 
        total += num

print(f'A foram digitados {qtde} números.\nA soma dos números digitados é: {total}.\nA média entre eles é {total/qtde}')