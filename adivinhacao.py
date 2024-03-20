import random

def jogar() :
    print("###### Bem vindo ao jogo de ADIVINHAÇÃO ######")
    max_rand = 10
    sorteio = random.randint(0, max_rand)

    ## CRIAR DIFICULDADES DIFERENTES. Exemplo:
    ## FÁCIL - 10 TENTATIVAS
    ## MÉDIO - 5 TENTATIVAS
    ## DIFICIL - 3 TENTATIVAS

    ## enquanto
    tentativa = 1
    max_tentativas = 3
    while(tentativa <= max_tentativas):
        chute = int(input("Tentativa {} de {} - Digite o seu chute, entre 0 e 10: \n".format(tentativa, max_tentativas)))
        acertou = chute == sorteio
        if (acertou) :
            print("Parabéns, você ganhou!")
            break
        elif (chute > sorteio) :
            print("O número sorteado é menor")
        elif (chute < sorteio) :
            print("O número sorteado é maior")
        tentativa = tentativa + 1

    print("##### FIM DO JOGO #####")


if (__name__ == '__main__'):
    jogar()