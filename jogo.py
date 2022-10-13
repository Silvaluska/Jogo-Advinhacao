# Importações do projeto
import mods as md
from random import randint

md.titulo('Bem vindo ao jogo de advinhação!')

numero_secreto = randint(0,100)

tentativa = 1
max_tentativas = 3

while tentativa <= max_tentativas:
    print(f'Tentativa {tentativa} de {max_tentativas}')
    chute = int(input('Digite um número de 1 a 100: '))
    if chute == numero_secreto:
        print('Você acertou')
        break
    elif chute > numero_secreto:
        print('Seu chute foi maior que o número secreto')
    elif chute < numero_secreto:
        print('Seu chute foi menor que o número secreto')
    tentativa += 1

print('Fim do Jogo')
