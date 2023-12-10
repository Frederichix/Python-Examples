#NUMEROS

#Integer
a = 5

#Float
a = 5.5


#Operadores Numéricos
#a = (a+a)   #Soma
#b = (b-b)   #Subtração
#c = (c*c)   #Multiplicação
#d = (d/d)   #Divisão
#e = (e%e)   #Resto da divisão
#f = (f**f)  #Potência

#Operadores de Comparação
a < 10      #Menor que
a > 10      #Maior que
a <= 10     #Menor ou igual que
a >= 10     #Maior ou igual que
a == 10     #Igual que
a != 10     #Diferente que

#Operadores Lógicos
#not         #Não
#and         #E
#or          #Ou


#1 – Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z:
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = (x**2 + y**2) / (x - y)**2
print(int(z))

#2 – Escreva um programa que receba o salário de um funcionário (float), e retorne o resultado do novo salário com reajuste de 35%.
salario = float(input("Digite o seu salário: "))
porcentagem_reajuste = 35/100
reajuste_total = (porcentagem_reajuste * salario)
salario_reajustado = (salario + reajuste_total)
print(f"Seu salário deverá ser reajustado para: {salario_reajustado}")



