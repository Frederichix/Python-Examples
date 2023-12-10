#LISTAS
#Conjunto sequencial de valores, onde cada valor é identificado através de indices.

lista_mista = [3, 'Abacate', 5.6, [4, 5, 6], "Pyhton", (3,'j')]
#              0      1       2       3          4        5             INDICES 

print(lista_mista[2])
print(lista_mista[3])
print(lista_mista[3] [2])
print(type(lista_mista[5]))

#Atribuindo valores a lista
lista_mista[3] = 'morango'
print(lista_mista[3])

#Funções para manipulações de listas
# print(len(lista_mista))                 #Retorna o tamanho da lista
# print(min(lista_mista))                 #Retorna o menor valor da lista
# print(max(lista_mista))                 #Retorna o maior valor da lista
# print(sum(lista_mista))                 #Retorna a soma dos elementos da lista
# print(lista_mista.append(100))          #Adiciona um novo valor ao final da lista
# print(lista_mista.extend([1,2,3]))      #Insere uma lista no final de outra lista
# del lista_mista[1]                      #Remove um elemento da lista
# 3 in lista_mista                        #Verifica se um valor pertence a lista
# print(lista_mista.sort())               #Ordena a lista em ordem crescente
# print(lista_mista.reverse())            #Inverte os elementos de uma lista

#Fatiamento de listas
L = [3, 'abacate', 3.4, [5,6,7], 9]
print(L[1:4])       #Seleciona os elementos da posição 1,2,3
print(L[2:])        #Seleciona os elementos da posição 2 em diante
print(L[:4])        #Seleciona os elementos até a posição 3

#Criação de listas com range
L1 = list(range(5))
print(L1)

L2 = list(range(3,8))
print(L2)

L3 = list(range(2,11,3))
print(L3)



#Exercicios
#1 – Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
#a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

L = [5, 7, 2, 9, 4, 1, 3]
print(len(L))
print(max(L))
print(min(L))
print(sum(L))
ordem_crescente = sorted(L)
print(ordem_crescente)
ordem_decrescente = sorted(L, reverse=True)
print(ordem_decrescente)

#2 – Gere uma lista de contendo os múltiplos de 3 entre 1 e 50.
lista_um_a_cinquenta = list(range(1,51,3))
print(lista_um_a_cinquenta)