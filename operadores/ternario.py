chovendo = False #Atribuindo valor logico false
Saldo = 58 # Atribuindo 58 para o saldo

""" Sabado será no parque se não estiver chovendo e saldo for maior que 50, 
 senão sabado será triste """

Sabado = 'no parque. :)' if chovendo == False and Saldo >= 50 else 'triste :(' 

print(f'Esse sabado será {Sabado}')

