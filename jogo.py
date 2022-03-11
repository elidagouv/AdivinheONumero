import random
from time import sleep
import sys
import os
from rich import print

#limpa o terminal (linux ou windows)
limpar = 'cls' if os.name == 'nt' else 'clear'
os.system(limpar)

print('-=-=-=- JOGO CONTRA O COMPUTADOR -=-=-=-')
tentativas = 0
n1 = int(random.randint(0, 10))
print('Sou o computador e vou jogar contra você!')
n2 = int(input('\nDigite um número entre 0 e 10: '))

##animação do ponto final "..."
pontos = '...'
print('Escolhendo aleatoriamente', end='')
for i in list(pontos):
    print(i, end='')
    sys.stdout.flush()
    sleep(1)

while n2 != n1:
    try:
        tentativas += 1
        n2 = int(input('\n\nErrou... Tente novamente: '))
        sleep(0.5)
        if n2 < n1:
            print(f'[red]O número é maior que {n2}.[/]')
        elif n2 > n1:
            print(f'[cyan]O número é menor que {n2}.[/]')
    except ValueError:
        print(
            'Erro!!!\nVocê digitou uma string, tente novamente!'
            )
else:
    print('-=-=-=-=-=-=-=-=-=-=-=-')
    print('Parabéns! Você venceu!')
    print('-=-=-=-=-=-=-=-=-=-=-=-')

print('O número escolhido por mim foi {}'.format(n1))
#SUGESTÃO > print(f'O número escolhido por mim foi {n1}')
print('Você levou {} tentativas para ganhar.'.format(tentativas))
#SUGESTÃO > print(f'Você levou {tentativas} tentativas para ganhar.')
