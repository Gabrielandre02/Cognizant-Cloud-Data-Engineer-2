import hashlib

string = input("Digte a texto a ser gerado a hash:")

menu = int(input('''### MENU - ESCOLHE O TIPO DE HASH ####
             1)MD5
             2)SHA1
             3)SHA256
             4)SHA512
             5)EXIT
             Digite o número do hash a ser gerado:'''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("A hash MD5 da {}, é {}".format(string, resultado.hexdigest()))
elif  menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("A hash SHA1 da {}, é {}".format(string, resultado.hexdigest()))
elif  menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("A hash SHA256 da {}, é {}".format(string, resultado.hexdigest()))
elif  menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("A hash SHA512 da {}, é {}".format(string, resultado.hexdigest()))
elif  menu == 5:
    exit
else:
    print('Algo deu errado, tente novamente')