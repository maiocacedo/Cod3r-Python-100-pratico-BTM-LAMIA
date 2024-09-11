from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 9.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.8},
]

aluno_aprovado = lambda aluno: aluno['nota'] >= 7
# aluno_honra = lambda aluno: aluno['nota'] >= 9
obter_nota = lambda aluno: aluno['nota'] 
somar = lambda a, b: a + b

alunos_aprovados = list(filter(aluno_aprovado, alunos))
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))
# alunos_honras = list(filter(aluno_honra, alunos))
total = reduce(somar, notas_alunos_aprovados, 0) # fazer a media em reduce!!

print('alunos: \n', *alunos, sep='\n', end='\n\n')
print('alunos aprovados: \n', *alunos_aprovados, sep='\n', end='\n\n')
print('Alunos aprovados notas: \n', notas_alunos_aprovados)
print(total / len(alunos_aprovados))
# print('alunos honrados: \n', *alunos_honras, sep='\n')

