a = 3
b = 4.4

print(a+b)

texto = "sua idade é... "
idade = 23

#print(texto + str(idade))
print (f'{texto} {idade}')

print(3 * 'bom dia')

PI = 3.14
raio = float(input('Informe o raio da circ? '))
print(type(raio))

#area = PI * raio * raio
area = PI * pow(raio, 2)
print(f'A área da circ é {area} m².')