primeiro = int(input('Informe o 1º termo da PA: '))
razao = int(input('Informe a razão dessa PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo}', end=' -> ')
    termo += razao
    cont += 1

print('ACABOU')
