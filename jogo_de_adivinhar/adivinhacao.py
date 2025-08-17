from random import randint

print('-'*6 ,'Jogo da adivinhação','-'*6)

print('\nObjetivo - Tente advinhar o número que a máquina vai escolher de 1 a 5')
print('Vidas: ❤ ❤ ❤ ') 

vidas = 3 

numero_aleatorio = randint(1,5)

while vidas > 0:
    num = int(input('Adivinhe o número: '))

    if num == numero_aleatorio:
        print('Parabéns! Você ganhou 🏆')
        break
    else:
        vidas -= 1
        print(f'Você errou restam {vidas} vidas')

        if vidas == 0:
            print('Fim de Jogo! você perdeu todas as vidas 💔 ')

