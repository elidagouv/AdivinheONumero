import random
from time import sleep

print('-=-=-=- JOGO CONTRA O COMPUTADOR -=-=-=-')
tentativas = 0
n1 = int(random.randint(0, 10))
print('Sou o computador e vou jogar contra você!')
n2 = int(input('Digite um número entre 0 e 10: '))
print('Escolhendo aleatoriamente...')
sleep(2)
while n2 != n1:
    tentativas += 1
    n2 = int(input('Errou... Tente novamente: '))
    sleep(0.5)
    if n2 < n1:
        print('O número é maior.')
    elif n2 > n1:
        print('O número é menor.')
else:
    print('-=-=-=-=-=-=-=-=-=-=-=-')
    print('Parabéns! Você venceu!')
    print('-=-=-=-=-=-=-=-=-=-=-=-')

print('O número escolhido por mim foi {}'.format(n1))
print('Você levou {} tentativas para ganhar.'.format(tentativas))