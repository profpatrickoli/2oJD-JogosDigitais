import adivinhacao
import forca

jogo = int(input("1 - ADIVINHAÇÃO 2 - FORCA \n"))


if jogo == 1 :
    adivinhacao.jogar()
else :
    forca.jogar()