# 1
# valor1 = int(input("Digite o primeiro valor:"))
# valor2 = int(input("Digite o segundo valor"))
#
# if valor1 > valor2:
#     print("Primeiro numero maior que o segundo ")
# else:
#     print("Segundo numeor é maior que o primeiro")

# 2
# anoDenascimento = int(input("Digite o sue ano de nascimento:"))
#
# resultado = 2024 - anoDenascimento
#
# if resultado >= 18:
#     print("Você pode votar esse ano")
# else:
#     print("Você não pode votar esse ano")

# 3
# senha = input("Digite sua senha: ")
# senha_correta = '1234'
# if senha == senha_correta:
#     print("Acesso Permitido!")
# else:
#     print("Acesso Negado")

# 4
# maca = int(input("Quantas maças vc ira comprar ? "))
# maca_preco = 0.30
#
# if maca > 12:
#     maca_preco = 0.25
#
# resultado = input(f"{maca * maca_preco}")

# 5
a = int(input("Diga o primeiro:"))
b = int(input("Diga o segundo:"))
c = int(input("Diga o terceiro:"))

if a>b and a>c:
    aux = a
    a = c
    c = aux
elif b>c:
    aux = c
    c = b
    b = aux
if a > b:
    aux = a
    a = b
    b = aux

print(a,b,c)
#6
# altura = float(input("Digite a altura:"))
# sexo = int(input("Digite o seu sexo (1 para feminino, 2 para masculino):"))
#
# if sexo == 1: #Feminino
#     peso_ideal = 62.1 * altura -44.7
# else: #Mascuino
#     peso_ideal = 72.7 * altura -58
#
# print(f"O peso ideal para uma pessoa de altura {altura:.2f}m e sexo {sexo} é {peso_ideal:.2f}kg.")

#7 e 8
# nm_lados = int(input("Diga o número de lados (3 para triangulo, 4 para quadrado e 5 para pentagono:"))
# comprimento = float(input("Diga o comprimento do poligono:"))
#
# if nm_lados < 3:
#     print("Isso não é um poligono")
# elif nm_lados == 3:
#     print(f"Isso é um triangulo / perimetro {comprimento * 3} ")
# elif nm_lados == 4:
#     print(f"isso é um quadrado / perimetro {comprimento * 4}")
# elif nm_lados == 5:
#     print(f"Isso é um pentagono / perimetro {comprimento * 5}")
# else:
#     print("poligono não indentificado")

#10
# ml = int(input("Diga o numero de lados (3 para trinagulo equilatero, 2 triangulo isosceles e 4 para escaleno: "))
# if ml ==3:
#     nome = "Equilatero"
# elif ml ==2:
#     nome = "Isosceles"
# else:
#     nome = "escaleno"
#
# print(f"Seu triangulo é um {nome}")

#11
# a1 = int(input("diga o valor do primeiro angulo: "))
# a2 = int(input("diga o valor do segundo angulo: "))
# a3 = int(input("diga o valor do terceiro angulo: "))
# if a1 ==90 or a2 == 90 or a3 ==90:
#     print("angulo reto")
# elif a1 > 90 or a2 > 90 or a3 ==90:
#     print("Angulo obtuso")
# else:
#     print("Angulo agudo")

# 9
# num1= int(input("Coloque o primeiro número:"))
# num2= int(input("Coloque o segundo número:"))
# num3= int(input("coloque o terceiro número:"))
#
# if (num1 > num2) and (num1 > num3):
#     resultado = num1
# elif (num2 > num3):
#     resultado = num2
# else:
#     resultado = num3
#
# print("O número maior é:", resultado)
