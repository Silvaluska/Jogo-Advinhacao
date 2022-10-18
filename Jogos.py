import mods as md
import advinhacao
import forca

while True:
    md.titulo('Escolha seu jogo')
    print('(1) Advinhação (2) Forca')
    jogo = input('Qual jogo você quer jogar: ')
    if jogo == '1':
        advinhacao.jogar()
    elif jogo == '2':
        forca.jogar()
    else:
        break