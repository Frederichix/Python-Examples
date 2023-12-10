#FUNÇÕES
#Funções são pequenos blocos de códigos reutilizáveis. Elas permitem dar um nome a um bloco de comandos e executar este bloco a partir de qualquer lugar do programa.

def hello():
    print("Olá mundo!")

hello()

#Parâmetros e Argumentos
                            #            var1,   var2 
def maior(x,y):             #def maior (param1, param2)
    if x>y:         #Argumentos
        print(x)
    else:
        print(y)

maior(4,7)


#Escopo das variáveis
def soma(x,y):
    global total                    #Para uma variável ser compartilhada entre diversas funções, ela deve
    total = x+y                     #ser definida como variável global
    print("Total soma=", total)

global total
total = 10
soma(3,5)
print("Total principal = ",total)


#Retorno de valores
def soma(x,y):
    total = x+y
    return total        #O comando return é usado para retornar um valor de uma função e encerrá-la

s=soma(3,5)
print("Soma= ",s)


#Valor padrão
def calcula_juros(valor, taxa=10):          #É possível definir um valor padrão para os parâmetros da func
    juros= valor*taxa/100
    return juros

print(calcula_juros(500))


#Exercícios
#1 - Crie uma função para desenhar uma linha, usando o caractere '_'. O tamanho da linha deve ser definido na chamada da função.

def linha(N):
    for i in range (N):
        print(end='_')
    print(" ")

linha(9)


#2 - Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A função deve imprimir todos os elementos da lista numerando-os.
L = [1,2,3,4,5,6,7,8,9]

def imprime_lista(L):
    contador = 0
    for valor in L:
        contador = contador + 1
        print(contador,')',valor)

print(imprime_lista(L))


#3 - Crie uma função que receba como parâmetro uma lista com valores numéricos e retorne a média desses valores.
lista = [3,4,1,4,5,6,7,2,10,11,18]

def media(lista):
    somador = 0
    for valor in lista:
        somador = somador + 1
    return somador / len(lista)

resultado = media(lista)
print(resultado)