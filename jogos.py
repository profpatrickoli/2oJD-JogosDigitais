import adivinhacao
import termo

jogo = int(input("1 - adivinhação 2 - termo \n"))


if jogo == 1 :
    print("executando adivinhacao")
    adivinhacao.jogar()
else :
    print("Executando termo")
    termo.jogar()