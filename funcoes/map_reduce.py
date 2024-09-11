from functools import reduce

def somar_nota(delta):
    def calc(nota):
        return nota + delta
    return calc

notas = [6.4, 7.2, 5.4, 8.4] # lista

notas_finais1 = list(map(somar_nota(1.5), notas))
notas_finais2 = list(map(somar_nota(1.6), notas))

print(notas_finais1, '  ', notas_finais2)


def somar(a, b):
    return a + b

total = reduce(somar, notas, 0)
print(total)

# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5
    
 
# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5
    