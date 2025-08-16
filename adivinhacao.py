from random import randint

print('-'*6 ,'Jogo da adivinhação','-'*6)

print('\nObjetivo - Tente advinhar o número que a máquina vai escolher de 1 a 5')
while True:
    num = int(input('Adivinhe o número: '))

    numero_aleatorio = randint(1, 5)

    print('O número escolhido foi:',numero_aleatorio)
    if num == numero_aleatorio:
        print('Parabéns! Você ganhou 👑')
        break

    else:
        print('Que pena! Você perdeu 🚫')

