import random

def jogar() :
    print("###### Bem vindo ao jogo de ADIVINHAÇÃO ######")
    ## Atividade 1 - CRIAR DIFICULDADES DIFERENTES:
    ## FÁCIL - 10 TENTATIVAS
    ## MÉDIO - 5 TENTATIVAS
    ## DIFICIL - 3 TENTATIVAS
    dificuldade = int(input("Digite a dificuldade desejada:\n1 - Fácil\n2 - Médio\n3 - Difícil\n"))
    if dificuldade == 1:
        max_tentativas = 10
        max_rand = 10
    elif dificuldade == 2:
        max_tentativas = 5
        max_rand = 10
    elif dificuldade == 3:
        max_tentativas = 5
        max_rand = 100
    else:
        print("Opção inválida, selecionado modo DIFÍCIL")
        max_tentativas = 5
        max_rand = 100
    
    sorteio = random.randint(0, max_rand)
    tentativa = 1
    while(tentativa <= max_tentativas):
        chute = int(input("Tentativa {} de {} - Digite o seu chute, entre 0 e {}: \n".format(tentativa, max_tentativas,max_rand)))
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
    print("O número sorteado era {}".format(sorteio))


if (__name__ == '__main__'):
    jogar()