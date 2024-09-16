# Criação de uma classe chama produto

class Produto:

# Função para inicializar a classe 

    def __init__(self, nome, preco = 1.99, desc=0): 
        self.nome = nome
        self.preco = preco
        self.desc = desc
   

    # Função para definir o desconto
	
    @property # Um decorador para tornar esse metodo em uma propriedade.
    def preco_final(self):
        return (1 - self.desc) * self.__preco
   

    # Função para definir preço

    @property # Um decorador para tornar esse metodo em uma propriedade.
    def preco(self):
        return  self.__preco
    
    # Função para aceitar modificações se o novo preço for maior que zero

    @preco.setter # Decorador utilizado para definir modificações no valor da propriedade.
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco

p1 = Produto('Caneta', 10.00, 0.1)  # Quando cria-se um objeto, ele é iniciado automaticamente. Produto.__init__(p1)
p2 = Produto('Caderno', 17.00, 0.5)

p1.preco = 0 # A Essa atribuição será desconsiderada pelo programa
p2.preco = 18.00 # Atribuindo novo preço ao caderno

print('Produto: ', p1.nome,' Preço: ',  p1.preco,' Desconto: ',  p1.desc, ' Preço final: ', p1.preco_final)
print('Produto: ', p2.nome,' Preço: ',  p2.preco,' Desconto: ',  p2.desc,' Preço Final: ', p2.preco_final)