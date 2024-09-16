# Criando classe carro

class Carro:
    # Iniciando classe	
    def __init__(self):
        self.__velocidade = 0
  
    # definindo velocidade
    @property
    def velocidade(self):
        return self.__velocidade
  
    # Função de acelerar que incrementa velocidade	
    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade
  
    # Função de frear que decrementa velocidade	
    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade
    
# Criando classe que tem como metodo herança a classe carro    
class Uno(Carro):
    pass

c2 = Uno()# atribuindo Uno ao objeto c2 

print('Dirigindo Uno...')

print(c2.acelerar())
print(c2.acelerar())
print(c2.acelerar())
print(c2.acelerar())
print(c2.frear())
print(c2.frear())
print(c2.frear())
print(c2.frear())

# Criando classe que tem como metodo herança a classe carro e redefindo a função acelerar somente nessa classe.
 
class Lancer(Carro):
    def acelerar(self):
        super().acelerar()
        return super().acelerar()

c1 = Lancer() # atribuindo Lancer ao objeto c1 

print('Dirigindo Lancer...')

print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())
print(c1.frear())
print(c1.frear())

