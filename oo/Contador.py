

class Contador:
    contador = 0
   
    # Função para incrementar o contador   

    @classmethod # Função que não acessa instância, mas acessa o objeto da classe

    def inc(cls):
        cls.contador += 1
        return cls.contador
   
   
    # Função para decrementar o contador    

    @classmethod # Função que não acessa instância self, mas acessa o objeto da classe
    def dec(cls):
        cls.contador -= 1
        return cls.contador

    # Função de incremento para n

    @staticmethod # Função que não acessa nem a instância self e nem o objeto da classe 
    def mais_um(n):
        return n + 1
   
   
  
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
print(Contador.mais_um(99))