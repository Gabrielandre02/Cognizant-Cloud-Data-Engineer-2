import paramiko
import time

arquivo = open("logs.txt", "a")
address = "34.125.7.189"
username = "root"
password = "Raivosa@02"

def ssh_connect(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=address, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    result = stdout.readlines()
    return result
    
check_status = ssh_connect('systemctl stop zabbix-agent && systemctl status zabbix-agent')

if check_status:
    for line in check_status:
        if 'Active' in line and 'running' in line:
            print(f"Serviço em execuçao")
        elif 'Active' in line and 'running' not in line:
            print(f"O serviço esta parado")
            print(f"Iniciando o processo de inicializaçao do serviço")
            start = ssh_connect('systemctl start zabbix-agent && systemctl status zabbix-agent')
            for line in start:
                start = (line.replace('\n', ''))
    
    result = (line.replace('\n', ''))
    arquivo.write(result + "\n")
    arquivo.write(start + "\n")
    arquivo.close()