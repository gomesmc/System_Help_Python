# Faça um mini-sistema que use interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer.
#Quando o usuário digitar 'fim', o programa irá encerrar. OBS: Use cores.

from time import sleep
c = ('\033[m',       # 0 - Sem cor
     '\033[0;30;41m', # 1 - Vermelho
     '\033[0;30;42m', # 2 - Verde
     '\033[0;30;43m', # 3 - Amarelo
     '\033[0;30;44m', # 4 - Azul
     '\033[0;30;45m', # 5 - Roxo
     '\033[0;30;47m'  # 6 - Cinza
)

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6],end='')
    help(com)
    print(c[0],end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

comando = ''
while True:
    titulo('Sistema de Ajuda: Help Python', 2)
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)
