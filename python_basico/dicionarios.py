#DICIONÁRIOS
#Conjunto de valores onde cada valor é associado a uma chave

itens_mercado = {
    "arroz" : 17.30,            #chave1 : valor1,
    "feijao" : 16.50,           #chave2 : valor2,
    "ovo" : 5.50,               #chave3 : valor3,
    "alface" : 3.30,            #chave4 : valor4,
    "macarrao" : 6.70           #chave5 : valor5
}

print(itens_mercado["arroz"])

#Acrescentando valores a lista
itens_mercado["carne"] = 15.50
itens_mercado["canjica"] = 6.32
print(itens_mercado)


#Operações em Dicionário
del itens_mercado["ovo"]        #Exclui item por chave
"feijao" in itens_mercado       #Verifica se a chave existe 
itens_mercado.keys()            #Devolve todas as chaves
itens_mercado.values()          #Devolve todos os valores

#Valores diversos
dx = {
    1 : "carro",
    2 : [3,4,5],
    7 : ('a','b'),
    4 : 173.7
}
print(dx[7])


#Exercicios
#1 – Dada a tabela a seguir, crie um dicionário que a represente:
# Lanchonete
# Produtos Preços R$
# Salgado R$ 4.50
# Lanche R$ 6.50
# Suco R$ 3.00
# Refrigerante R$ 3.50
# Doce R$ 1.00

lanchonete = {
    "salgado" : 4.50,
    "lanche" : 6.50,
    "suco" : 3.00,
    "refrigerante" : 3.50,
    "doce" : 1.00
}

# #2 – Considere um dicionário com 5 nomes de alunos e suas notas. Escreva um programa que calcule
# a média dessas notas.

notas = {
    "aluno1" : 5,
    "aluno2" : 9,
    "aluno3" : 4,
    "aluno4" : 7,
    "aluno5" : 10
}

valores = notas.values()
print(valores)

media = sum(valores) / len(valores)
print(media)