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


alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >=7]
notas_alunos_aprovados = [alunos['nota'] for aluno in alunos_aprovados]
media = lambda a, b: (a + b) /  len(alunos_aprovados)

total = reduce(media, notas_alunos_aprovados, 0) 

print('alunos: \n', *alunos, sep='\n', end='\n\n')
print('alunos aprovados: \n', *alunos_aprovados, sep='\n', end='\n\n')
print('Alunos aprovados notas: \n', notas_alunos_aprovados)
print(total)
# print('alunos honrados: \n', *alunos_honras, sep='\n')

