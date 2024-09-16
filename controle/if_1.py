
# Atribuindo uma entrada do usuário de tipo de ponto flutante em nota

nota = float(input('Informe a nota do aluno: '))

# Atribuindo valor logico verdadeiro a comportado se a entrada do usuário for s se não atribui-se valor falso

comportado = True if input('Ele se comportou? Responda com s ou n: ') == 's' else False

# Se a nota do aluno for maior que 7 e seu comportamendo for bom, ele será aprovado e adicionado ao quadro de honra
 
if nota > 7 and comportado:
    print('\nAprovadíssimo!\n') 
    print(f'Sua nota foi {nota}, Parabens!!')
    print('Pelo otimo comportamento, você estará no quadro de honra!')

# Senão, se a nota for maior ou igual a 6, o aluno está aprovado       

elif nota >= 6.0:
    print('\nAprovado!\n')
    print(f'Sua nota foi {nota}, Parabéns!!')
    
# Senão, se a nota for maior ou igual a 5, o aluno está de recuperação

elif nota >= 5.0:
    print('\nRecuperação\n')
    print(f'Sua nota foi {nota}, boa sorte na recuperação!')

# Senão, se a nota for maior ou igual a 6, o aluno está de recuperação e terá um trabalho para fazer

elif nota >= 3.0:
    print('\nRecuperação e Trabalho\n')
    print(f'Sua nota foi {nota}, boa sorte na recuperação e no trabalho')
    
# Senão, o aluno está reprovado 

else:
    print('Reprovado')
    print(f'Sua nota foi {nota}, infelizmente você está reprovado, sinto muito.')    
    