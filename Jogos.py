import mods as md
import advinhacao

md.titulo('Escolha seu jogo')
print('(1) Advinhação (2) Forca')
jogo = input('Qual jogo você quer jogar: ')

if jogo == '1':
    advinhacao.advinhacao()
elif jogo == '2':
    print('Ainda estamos desenvolvendo este jogo')