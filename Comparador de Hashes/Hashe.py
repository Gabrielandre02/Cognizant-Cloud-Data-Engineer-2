import hashlib

arquivo = "./a.txt"
arquivo1 = "./b.txt"

texto1 = 'texto 1'
texto2 = 'texto 2'

hash1 = hashlib.new('ripemd160')
hash2 = hashlib.new('ripemd160')


hash1.update(open(arquivo, 'rb').read())
hash2.update(open(arquivo1, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O (arquivo: {texto1}) é diferente do (arquivo {texto2})')
    print('O hash do arquivo text1 é:', hash1.hexdigest())
    print('O hash do arquivo text2 é:', hash1.hexdigest())
else:
    print(f'O (arquivo: {texto1}), é igual ao : (arquivo {texto2})')
    print('O hash do arquivo text1 é:', hash1.hexdigest())
    print('O hash do arquivo text2 é:', hash1.hexdigest())