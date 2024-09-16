def soma(*nums):
    total = 0 
    for n in nums:
        total += n
    return total

somar = soma(3, 2, 3, 5, 2)
print('3 + 2 + 3 + 5 + 2 = ', somar)

def resultado_final(**kwargs):
    status = 'aprovado(a)' if kwargs['nota'] >= 7.0 else 'reprovado(a) '
    return f'{kwargs["nome"]} foi {status}'

print(resultado_final(nome = "Caio", nota = 7.0)) 
