class Carro:
    def __init__(self):
        self.__velocidade = 0
  
  
    @property
    def velocidade(self):
        return self.__velocidade
  
  
    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade
  
  
    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade
    
    
class Uno(Carro):
    pass


class Ferrari(Carro):
    def acelerar(self):
        super().acelerar()
        return super().acelerar()

c1 = Ferrari()

print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())
print(c1.frear())
print(c1.frear())
