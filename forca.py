import random #importa a biblioteca com funções de números randômicos
def jogar() :
    # INICIALIZAÇÃO DE VARIÁVEIS
    palavras = [] # cria o array palavras, lista de palavras
    letras_acertadas = [] # cria o array com as letras que a pessoa acertou
    acertou = False # booleano para controlar o acerto
    enforcou = False # booleano para controlar o erro
    max_erros = 6 # variável que guarda o número máximo de erros.
    erros = 0 # variável que guarda cada erro do usuário

    # ABERTURA DE ARQUIVO COM PALAVRAS
    arquivo = open("frutas.txt", "r") # abre o arquivo frutas, e armazena ele na variável arquivo
    for linha in arquivo: # (laço de repetição) para cada linha do arquivo, executa alguma coisa
        palavras.append(linha.strip()) # adiciona a linha lida ao array palavras
    palavra_secreta = random.choice(palavras) # sorteia uma palavra, e armazena na variável palavra_secreta

    # PREENCHE O ARRAY DAS LETRAS ACERTADAS COM "_"
    for letra in palavra_secreta: # percorre cada letra da palavra secreta
        letras_acertadas.append("_") # adiciona o _ para cada letra
    
    # INÍCIO DO JOGO DA FORCA
    print("###### Bem vindo ao jogo da FORCA ######") # imprime para o usuário uma mensagem de bem vindo
    while(not acertou and not enforcou): # laço de repetição principal do jogo, repete enquanto o usuário não acertar e não enforcar
        print(letras_acertadas) # imprime na tela os _, para mostrar quantas letras tem a palavra
        print("Você tem {} tentativas!".format(max_erros - erros)) # imprime quantas tentativas o usuário possui
        chute = input("Digite a letra\n") # entrada de texto do usuário. O que for digitado será salvo como chute
        chute = chute.strip() # remove caracteres especiais do chute
        index = 0 # variável de início para verificar a posição da letra
        if chute in palavra_secreta: # verifica se o chute está dentro da palavra_secreta
            for letra in palavra_secreta: # laço de repetição: percorre cada letra da palavra_secreta
                if (chute.upper() == letra.upper()): # verifica se o chute é igual a letra que está percorrendo
                    letras_acertadas[index] = chute.upper() #  coloca o chute do usuário dentro do array letras_acertadas         
                index = index + 1 # Variável que armazena o índice da letra, somando a cada letra conferida
        else: # se o chute não estiver na palavra
            erros = erros + 1 # adiciona + 1 nos erros

        if letras_acertadas.count("_") == 0: # verifica se não existe _ nas letras acertadas
            acertou = True # coloca verdadeiro na variável acertou
            print(letras_acertadas) # imprime na tela as letras que o jogador acertou
            print("Parabéns, você acertou a palavra! A palavra correta era", palavra_secreta)
        
        if (erros == max_erros): # se erros do usuário for igual ao máximo de erros
            enforcou = True # coloca verdadeiro na variável enforcou
            print(letras_acertadas) # imprime as letras acertadas
            print("A palavra correta era", palavra_secreta) # imprime um texto + a palavra secreta
    print("##### FIM DO JOGO #####") # imprime na tela o texto


if (__name__ == '__main__'):
    jogar()