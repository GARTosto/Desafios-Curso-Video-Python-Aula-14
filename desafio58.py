import random

print('Sou seu computador ...Acabei de penser em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
computador = random.randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')

print(f'Você acertou mas precisou de {palpites} tentativas para vencer. Parabéns!')
