import random

def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de adivinhação!")
    print("*********************************")

    #Variável
    numeroSecreto = random.randrange(1,101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("(1) Fácil, (2) Médio, (3) Difícil")
    nivel = int(input("Digite o nível de dificuldade: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    print(numeroSecreto)

    #Estrutura de Repetição
    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa: {rodada} de {total_de_tentativas}")
        chute_str = input("Digite o número entre 1 e 100: ")                
        print(f"Você digitou: {chute_str}")
        chute = int(chute_str)

        acertou = chute == numeroSecreto
        maior = chute > numeroSecreto
        menor = chute < numeroSecreto

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número ENTRE 1 e 100!")

        #Estrutura de Condição
        if(acertou):
            print("Você acertou!")
            break
        else:
            pontos_perdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Você errou. O seu chute foi maior que o número secreto!")
            elif(menor):
                print("Você errou. O seu número foi menor que o número secreto!")

        print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()
