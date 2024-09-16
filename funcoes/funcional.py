# Função para somar argumento a com b

def soma(a, b):
    return a + b


# Função para multiplicar argumento a com b
 
def multiplicacao(a, b):
    return a * b



somar = soma # Atribuindo função soma ao objeto somar
print(somar(3,4)) # Exibindo soma de 3 com 4


# Definindo uma função com outra função como parametro, e retornando o resultado dessa função com os parametro op1 e op2.

def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)


resultado = operacao_aritmetica(soma, 13, 48)
print(resultado)

resultado2 = operacao_aritmetica(multiplicacao, 20, 10)
print(resultado2)


# Definindo soma com duas funções para que o processamento seja mais rapido

def soma_parcial(a):
    # processamento pesado 1 - 10s
    # processamento pesado 2 - 10s
    # processamento pesado 3 - 40s
    def concluir_soma(b):
        return a + b
    return concluir_soma

# r1 = soma_total(1, 2) => 1m10s
# r2 = soma_total(1, 3) => 1m10s
# r3 = soma_total(1, 4) => 1m10s
#3m30s

soma_1 = soma_parcial(1) # 1m
r1 = soma_1(2)  # 10s
r2 = soma_1(3)  # 10s
r3 = soma_1(4)  # 10s  
# 1m 30s

resultado_final = soma_parcial(10)(12)

print(resultado_final, r1, r2, r3)
