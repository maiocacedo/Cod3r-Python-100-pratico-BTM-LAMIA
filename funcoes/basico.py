
def saudacao(nome = 'Pessoa', idade = 20):
    print(f'Bom dia, {nome}, de {idade} anos de idade! Você é incrível!')


def soma_e_multi(a, b, x):
    return a + b * x


saudacao()


if __name__ == '__main__': 
    saudacao('Maria Luiza', 18)

    
y = soma_e_multi(1, 2, 3)
print('\n1 + 2 * 3 = ', y)    
