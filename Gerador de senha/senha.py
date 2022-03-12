import random, string

tamanho = int(input('Digite o tamanho da senha desejada:'))

chars = string.ascii_letters + string.digits + '!@$%^,;(){}?'

rnd = random.SystemRandom()

p = ''.join(rnd.choice(chars) for i in range(tamanho))
print('A eenha que gerada tem o tamanho de  {} caracteres, resultando em: {}'.format(tamanho, p))