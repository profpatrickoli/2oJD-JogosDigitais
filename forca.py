import random
def jogar() :
    palavras = []
    arquivo = open("frutas.txt", "r")
    for linha in arquivo:
        palavras.append(linha.strip())
    palavra_secreta = random.choice(palavras)
    #print(palavras)

    print("###### Bem vindo ao jogo da FORCA ######")
    letras_acertadas = []
    for letra in palavra_secreta:
        letras_acertadas.append("_")
    acertou = False
    enforcou = False
    max_erros = 6
    erros = 0

    while(not acertou and not enforcou):
        print(letras_acertadas)
        print("Você tem {} tentativas!".format(max_erros - erros))
        chute = input("Digite a letra\n")
        chute = chute.strip()
        index = 0
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = chute.upper()           
                index = index + 1
        else:
            erros = erros + 1

        if letras_acertadas.count("_") == 0:
            acertou = True
            print(letras_acertadas)
            print("Parabéns, você acertou a palavra! A palavra correta era", palavra_secreta)
        
        if (erros == max_erros):
            enforcou = True
            print(letras_acertadas)
            print("A palavra correta era", palavra_secreta)
    print("##### FIM DO JOGO #####")


if (__name__ == '__main__'):
    jogar()