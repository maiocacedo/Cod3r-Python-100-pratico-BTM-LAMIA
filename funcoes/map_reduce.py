# Função para definir incrementar a nota do aluno com o bonus delta


def somar_nota(delta):
    def calc(nota):
        return nota + delta
    return calc

notas = [6.4, 7.2, 5.4, 8.4] # lista

notas_finais1 = list(map(somar_nota(1.5), notas))
notas_finais2 = list(map(somar_nota(1.6), notas))

print(notas_finais1, '  ', notas_finais2)

from functools import reduce

nums = [6.0, 12, 7.4] # lista de números

# Função para somar a com b
def somar(a, b):
    return a + b

# Reduce para percorrer a lista de números e aplicar a função soma neles
total = reduce(somar, nums, 0)
print('6 + 12 + 7.4 = ', total)