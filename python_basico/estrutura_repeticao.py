#ESTRUTURAS DE REPETIÇÃO
#É utilizada para executar uma mesma sequência de comandos várias vezes. A repetição está associada ou a uma condição, que indica se deve continuar ou não. São conhecidas também como loops.

senha = '12345'
leitura = " "

while (leitura != senha):
    leitura = input("Digite a senha: ")
    if leitura == senha:
        print("Acesso liberado")
    else:
        print("Senha incorreta. Tente novamente!")

contador = 0
somador = 0

while contador < 5:
    contador = contador + 1
    valor = float(input('Digite o '+str(contador)+'° valor:'))
    somador = somador + valor
print('Soma = ', somador)


#Laço for
#Estrutura de repetição mais utilizada. Pode ser com uma sequência numérica ou associado a uma lista.

#Exemplo: Encontrar a soma S= 1+4+7+10+13+16+19

S = 0
for x in range(1,20,3):
    S = S+x
    print('Soma = ', S)

lista_notas = [3.4, 6.6, 8, 9, 10, 9, 9.5, 8.8, 4.3]
soma = 0
for nota in lista_notas:
    soma = soma+nota
media = soma/len(lista_notas)
print("Média: ", media)


#Exercicios
#1 - Escreva um programa para encontrar a soma S = 3 + 6 + 9 + …. + 333.
S = 0
for x in range(3,334,3):
    S = S+x
print("Soma: ", S)

#2 – Escreva um programa que leia 10 notas e informe a média dos alunos.
S = 0
for contador in range(1,11):
    nota = float(input("Digite a nota "+str(contador)+": "))
    S = S+nota
print("Média = ", S/10)

#3 – Escreva um programa que leia um número de 1 a 10, e mostre a tabuada desse número.
numero = int("Digite o número para tabauda: ")
for sequencia in range(1,11):
    print("%2d x %2d = %3d" %(sequencia,numero,sequencia*numero))



