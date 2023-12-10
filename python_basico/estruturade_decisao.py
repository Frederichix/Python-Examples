#ESTRTUTURAS DE DECISÃO
#Alteram o fluxo de execução de um programa.

#if     se
#elif   senão
#else   senão se

valor = int(input("Qual sua idade? : "))
if valor < 18:
    print("Você é menor de idade")
else:
    print("Você é maior de idade")


valor = int(input("Qual sua idade? : "))
if valor < 6:
    print("Que coisa fofa")
elif valor < 18:
    print("Você ainda não pode dirigir")
elif valor > 60:
    print("Você está na melhor idade")
else:
    print("Você é o cara")


#Exercicios
#1 – Faça um programa que leia 2 notas de um aluno, calcule a média e imprima aprovado ou reprovado (para ser aprovado a média deve ser no mínimo 6)

nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 6:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")

#2 – Refaça o exercício 1, identificando o conceito aprovado (média superior a 6), exame (média entre 4 e 6) ou reprovado (média inferior a 4).

nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 6:
    print("Você foi aprovado")
elif media >= 4 and media < 6:
    print("Você ficou de exame")
else:
    print("Você foi reprovado")
