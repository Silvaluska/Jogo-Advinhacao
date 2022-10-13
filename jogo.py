# Importações do projeto
import mods as md
from random import randint

md.titulo('Bem vindo ao jogo de advinhação!')

numero_secreto = randint(0,100)

max_tentativas = 3

for tentativa in range(1, max_tentativas + 1):
    print(f'Tentativa {tentativa} de {max_tentativas}')
    chute = int(input('Digite um número de 1 a 100: '))
    if 0 <= chute <= 100:
        if chute == numero_secreto:
            print('Você acertou')
            break
        elif chute > numero_secreto:
            print('Seu chute foi maior que o número secreto', numero_secreto)
        elif chute < numero_secreto:
            print('Seu chute foi menor que o número secreto')
    else:
        print('Você digitou um número invalido')
        tentativa -= 1

print('Fim do Jogo')
