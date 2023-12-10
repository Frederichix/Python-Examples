import python_game.forca as forca
import python_game.adivinhacao as adivinhacao

def seleciona_jogos():
    print("(1) Adivinhação, (2) Forca")
    jogo = int(input("Digite a opção: "))

    if(jogo == 1):
        adivinhacao.jogar()
    elif(jogo == 2):
        forca.jogar()
    else:
        print("Numero inválido")

if(__name__ == "__main__"):
    seleciona_jogos()

