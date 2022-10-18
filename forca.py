from random import choice

def jogar():
    #Importações do projeto
    import mods as md
    
    # Titulo do jogo
    md.titulo('Jogo da forca')

    # Variaveis iniciais do jogo
    palavra_secreta = escolhe_palavra_secreta()
    letras_acertadas = ['_' for letra in palavra_secreta] 

    # Condições iniciais do jogo
    enforcou = False
    acertou = False
    erros = 0

    # Laço para fazer a analise das palavras chutadas
    while not enforcou and not acertou:
        mostra_acertos(letras_acertadas)
        chute = input('Digite uma letra: ').strip().upper()
        posicao = 1
        if chute in palavra_secreta:
            acrescenta_chute(palavra_secreta, chute, letras_acertadas, posicao)
        else:
            erros += 1
            print(f'Você ainda tem {7-erros} tentativas antes de ser enforcado')
            desenha_forca(erros)
        acertou = verifica_se_ganhou(letras_acertadas, palavra_secreta)
        enforcou = verifica_se_perdeu(erros, palavra_secreta)

    print('Fim do jogo')

def escolhe_palavra_secreta():
    lista_palavras = []
    with open('palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip().upper()
            lista_palavras.append(linha)
    return choice(lista_palavras)

def mostra_acertos(letras_acertadas):
    print()
    for letras in letras_acertadas:
        print(letras, end=' ')
    print()
    print()

def acrescenta_chute(palavra_secreta, chute, letras_acertadas, posicao):
    for letra in palavra_secreta:
        if letra == chute:
            letras_acertadas[posicao-1] = chute
        posicao += 1

def imprime_mensagem_vencedor(palavra_secreta):
    print("A palavra era {}".format(palavra_secreta))
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def verifica_se_ganhou(letras_acertadas, palavra_secreta):
    if '_' not in letras_acertadas:
        imprime_mensagem_vencedor(palavra_secreta)
        return True

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def verifica_se_perdeu(erros, palavra_secreta):
    if erros == 7:
        imprime_mensagem_perdedor(palavra_secreta)
        return True

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == '__main__':
    jogar() 
