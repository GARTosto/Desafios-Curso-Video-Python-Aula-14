import time

num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
print('''O que deseja realizar com esses valores? Digite uma das opções abaixo:
[1] somar os números
[2] multiplicar os números 
[3] verificar qual dos valores é o maior
[4] digitar novos números
[5] sair do programa. ''')

option = int(input('Digite a opção desejada: '))

while option != 5:
    if option == 1:
        print(f'A soma de {num1} com {num2} deu {num1 + num2}.')
    if option == 2:
        print(f'{num1} multiplicado por {num2} dá {num1 * num2}.')
    if option == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}.')
        elif num2 > num1:
            print(f'{num2} é maior que {num1}.')
        else:
            print('Você digitou números iguais.')
    if option == 4:
        print('Você escolheu digitar novos valores.')
        num1 = float(input('Digite o novo valor: '))
        num2 = float(input('Digite o novo valor: '))
    if option > 5:
        print('Opção inválida. Tente novamente.')

    option = int(input('Digite outra opção ou digite [5] para sair do programa: '))

time.sleep(1)
print('Finalizando...')
print('Obrigado por participar!')

