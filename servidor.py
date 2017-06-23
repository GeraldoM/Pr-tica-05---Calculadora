import socket
from math import sqrt

def is_float(valor):
	try:
		float(valor)
		return True
	except ValueError:
		return False
 

#Variaveis de apoio
HOST = socket.gethostbyname('localhost')
PORT = 3000

#Instanciando transporte TCP/IP
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Associacao de porta ao processo servidor
tcp_server_socket.bind((HOST,PORT))
tcp_server_socket.listen(999)
print("Servidor online!")


while True:
	client, addr = tcp_server_socket.accept()
	conectado = False
	while True:
		#Recebe os dados do cliente
		if conectado == False:
			print("Cliente conectado!\nEndereço do cliente: " + str(addr[0]) + "\nPorta: " + str(PORT) + "\n")
			conectado = True
		data = client.recv(2048)
		data = data.decode('utf-8')
		print("Comando recebido: " + data)
		data = data.split()
		if data[0] == 'soma' and len(data) == 3 and is_float(data[1]) and is_float(data[2]):
			arg1 = float(data[1])
			arg2 = float(data[2])
			resultado = str(arg1+arg2)
			message = ("A soma é " + resultado)
			byte_msg = message.encode('utf-8')
			#Envio da mensagem de resultado da soma
			client.send(byte_msg)
		elif data[0] == 'raiz_quadrada' and len(data) == 2 and data[1].isdigit():
			arg = int(data[1])
			resultado = str(sqrt(arg))
			message = ("A raiz é " + resultado)
			byte_msg = message.encode('utf-8')
			#Envio da mensagem de resultado da raiz
			client.send(byte_msg)
		elif str(data[0]) == 'exit':
			message = ("Conexão encerrada!")
			print(message[0:-1] + " pelo cliente!")
			byte_msg = message.encode('utf-8')
			#Envio da mensagem de encerramento
			client.send(byte_msg)
			break
		else:
			#Preparo mensagem de comando inválido
			message = "Mensagem inválida."
			byte_msg = message.encode('utf-8')
			#Envio da mensagem de comando inválido
			client.send(byte_msg)

	break
		#print("\n Mensagem recebida:", data)
	
	
client.close()
tcp_server_socket.close()
