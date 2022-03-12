import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("a conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()
    
    print("Socket criado com sucesso")
    
    hostalvo = input("Digite o Host ou ip a ser conectado:")
    portaalvo = input("Digite a porta a ser conectada:")
    
    try:
        s.connect((hostalvo, int(portaalvo)))
        print("Cliente TCP conectado com sucesso\
            no host: {} e na porta {}".format(hostalvo, portaalvo))
        s.shutdown(2)
    except socket.error as e:
        print("nao foi possivel conectar no hots: {} e na porta {}".format(hostalvo, portaalvo))
        print("Erro: {}".format(e))
        sys.exit()
        
        
if __name__ == '__main__':
    main()