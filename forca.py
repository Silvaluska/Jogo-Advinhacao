def jogar():
    #Importações do projeto
    import mods as md
    
    # Titulo do jogo
    md.titulo('Jogo da forca')

    # Variaveis iniciais do jogo
    palavra_secreta = 'BANANA'
    letras_acertadas = []
    for letra in palavra_secreta:
        letras_acertadas.append('_') 

    # Condições iniciais do jogo
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        print(letras_acertadas)
        chute = input('Digite uma letra: ').strip().upper()
        posicao = 1
        for letra in palavra_secreta:
            if letra == chute:
                letras_acertadas[posicao-1] = chute
            posicao += 1
        if '_' not in letras_acertadas:
            print('Parabens, Você conseguiu descobrir a palavra')
            break

    print('Fim do jogo')

if __name__ == '__main__':
    jogar() 