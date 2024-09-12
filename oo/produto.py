
class Produto:
    def __init__(self, nome, preco = 1.99, desc=0):
        self.nome = nome
        self.preco = preco
        self.desc = desc
    
    @property
    def preco_final(self):
        return (1 - self.desc) * self.__preco
    
    @property
    def preco(self):
        return  self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco

p1 = Produto('Caneta', 10.00, 0.1)  # Produto.__init__(p1)
p2 = Produto('Caderno', 12.99, 0.5)

p1.preco = 1.2
p2.preco = -123

print('Produto: ', p1.nome,' Preço: ',  p1.preco,' Desconto: ',  p1.desc, ' Preço final: ', p1.preco_final)
print('Produto: ', p2.nome,' Preço: ',  p2.preco,' Desconto: ',  p2.desc,' Preço Final: ', p2.preco_final)