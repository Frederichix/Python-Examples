#STRINGS
a = "a"

#Concatenação de Strings
print("Apostila"+"Python")
e = "!@#$%*"

#Manipulação de Strings
teste = "Apostila de Python"
len(teste)                      #Retorna o tamanho da String
teste.capitalize()              #Retorna a primeira String com letras maiúsuclas
teste.count("a")                #Retorna quantas vezes a string aparece
teste.startswith("Ap")          #Verifica se a String inicia com determinada sequência
teste.endswith("on")            #Verifica se a String termina com determinada sequência
e.isalnum()                     #Verifica se a String possui algum alfanúmerico
teste.isalpha()                 #Verifica se a String possui algum alfanúmerico (letra ou número)
teste.islower()                 #Verifica se a String só possuem letras minúsculas
teste.isupper()                 #Verifica se a String possui todas letras minúsculas
teste.lower()                   #Retorna a String colocando em letras minúsculas
teste.swapcase()                #Inverte o conteúdo da String (Maiuscula/Minuscula)
teste.title()                   #Converte para maíusculo todas as primeiras letras
teste.split()                   #Transforma a String em uma lista
teste.replace("teste", "Py")    #Troca uma palavra do texto para outra
teste.find("h")                 #Retorna o Índice da primeira ocorrência
teste.ljust(12)                 #Acrescenta espaços a esquerda
teste.rjust(12)                 #Acrescenta espaços a direita
teste.center(10)                #Centraliza String
teste.lstrip()                  #Remove todos os espaços em branco do lado esquerdo da String
teste.rstrip()                  #Remove todos os espaços em branco do lado direito da String
teste.strip()                   #Remove todos os espaços em branco da String

#Fatiamento de Strings
s = "python"
s[1:4]              #Seleciona os elementos das posições 1,2,3
s[2:]               #Seleciona os elementos a partir da posição 2
s[:4]               #Seleciona os elementos até a posição 3

#Exercicios
#1 – Considere a string A = "Um elefante incomoda muita gente". Que fatia corresponde a "elefante incomoda?"
string_a = "Um elefante incomoda muita gente"
print(string_a[3:20])

#2 - Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em maiúscula e sem espaços em branco
frase = input("Escreva uma frase: ")
frase_maiuscula = frase.upper()
frase_sem_espaco = frase_maiuscula.replace(' ', '')
print(frase_sem_espaco)
