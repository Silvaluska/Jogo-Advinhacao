def jogar():
    #Importações do projeto
    import mods as md
    from random import choice
    
    # Titulo do jogo
    md.titulo('Jogo da forca')

    # Variaveis iniciais do jogo
    lista_palavras = []
    with open('palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip().upper()
            lista_palavras.append(linha)

    palavra_secreta = choice(lista_palavras)
    letras_acertadas = ['_' for letra in palavra_secreta] 

    # Condições iniciais do jogo
    enforcou = False
    acertou = False
    erros = 0

    # Laço para fazer a analise das palavras chutadas
    while not enforcou and not acertou:
        print()
        for letras in letras_acertadas:
            print(letras, end=' ')
        print()
        print()
        chute = input('Digite uma letra: ').strip().upper()
        posicao = 1
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if letra == chute:
                    letras_acertadas[posicao-1] = chute
                posicao += 1
        else:
            erros += 1
            print(f'Você ainda tem {6-erros} tentativas antes de ser enforcado')
        if '_' not in letras_acertadas:
            print(letras_acertadas)
            print('Parabens, Você conseguiu descobrir a palavra')
            acertou = True
        if erros == 6:
            print('Você foi enforcado')
            enforcou = True

    print('Fim do jogo')

if __name__ == '__main__':
    jogar() 