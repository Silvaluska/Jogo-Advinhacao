def jogar():
    # Importações do projeto
    import mods as md
    from random import randint

    # Inicio do programa onde é mostrado o titulo do programa e os niveis de dificuldade
    md.titulo('Bem vindo ao jogo de advinhação!')

    numero_secreto = randint(0,100) # geração aleátoria de um número de 0 a 100
    pontos = 100 # número de pontos

    print('Escolha seu nivel de dificuldade')
    print('(1) Facil (2) Médio (3) Dificil')

    # Escolha do nivel de dificuldade pelo usuário. obs: enquanto o usuário não escolher entre os niveis 1, 2 e 3 ele ficará preso em um loop infinito
    while True:
        nivel = input('Qual nivel de dificuldade você quer jogar: ')
        if nivel == '1':
            max_tentativas = 20
            break
        elif nivel == '2':
            max_tentativas = 10
            break
        elif nivel == '3':
            max_tentativas = 5
            break
        else:
            print('Este nivel de dificuldade não existe.')

    # Comparação do valor gerado pelo computador com o valor que será escolhido pelo usuário. obs: o número de tentativas é definido pelo nivel de dificuldade escolhido acima.
    for tentativa in range(1, max_tentativas + 1):
        print(f'Tentativa {tentativa} de {max_tentativas}')
        chute = int(input('Digite um número de 1 a 100: '))
        if 0 <= chute <= 100:
            if chute == numero_secreto:
                print('Você acertou')
                print(f'Você terminou o jogo com {pontos} pontos')
                break
            elif chute > numero_secreto:
                print('Seu chute foi maior que o número secreto')
                pontos -= md.pontos_perdidos(chute, numero_secreto)
            elif chute < numero_secreto:
                print('Seu chute foi menor que o número secreto')
                pontos -= md.pontos_perdidos(chute, numero_secreto)
        else:
            print('Você digitou um número invalido')
            tentativa -= 1
        if pontos <= 0:
            print('Você não tem mais pontos')
            break

    # Fim do jogo
    print('Fim do Jogo')

# Codigo para que possar executar o jogo de advinhação diretamente pelo terminal.
if __name__ == '__main__':
    jogar()
