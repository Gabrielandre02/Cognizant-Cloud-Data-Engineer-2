import os # Importar biblioteca 

print("#" * 60) 

ip_ou_host = input('Digite o Ip ou host a ser verificado')#variavel que recebe o ip

print("-" * 60)
os.system('ping -n 6 {}'.format(ip_ou_host))#funçao pra biblioteca pra pingar o host 

print("-" * 60)