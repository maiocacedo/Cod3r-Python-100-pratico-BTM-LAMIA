from functools import reduce

# Definindo dicionário

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 9.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 5.1},
    {'nome': 'Rafael', 'nota': 6.2},
]
# lambda para definir um aluno aprovado como sendo com nota >= 7
aluno_aprovado = lambda aluno: aluno['nota'] >= 7

# lambda para definir um aluno honrado como sendo com nota >= 9  
aluno_honra = lambda aluno: aluno['nota'] >= 9

# Lambda para definir obter_nota como sendo a nota do aluno 
obter_nota = lambda aluno: aluno['nota']

somar = lambda a, b: a + b

# Atribuindo a alunos aprovados uma lista filtrando somente os alunos aprovados.
alunos_aprovados = list(filter(aluno_aprovado, alunos))

# Atribuindo a notas_alunos_aprovados uma lista que mapeia a nota dos alunos aprovados pelo dicionário.
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))

# Atribuindo a alunos_honras uma lista somente com alunos honrados. 
alunos_honras = list(filter(aluno_honra, alunos)) 

# Atribuindo para total a media da soma de todas as notas dos alunos aprovados utilizando reduce. 
total = reduce(somar, notas_alunos_aprovados, 0) / len(alunos_aprovados)

print('alunos: \n', *alunos, sep='\n', end='\n\n')
print('alunos aprovados: \n', *alunos_aprovados, sep='\n', end='\n\n')
print('Alunos aprovados notas: \n', notas_alunos_aprovados)
print(total)
print('alunos honrados: \n', *alunos_honras, sep='\n')


