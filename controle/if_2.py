a = 'valor' # True
a = 0 # False
a = -0.001 # True
a = '' # False
a = ' ' # True
a = [] # False
a = {} # False

print(not not 'valor')

if a:
    print('Existe!!!')
else:
    print('não existe ou é zero ou é vazio')