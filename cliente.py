import socket
HOST = socket.gethostbyname('localhost')
PORT = 3000

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Estrutura inicial do client TCP/IP
tcp_client_socket.connect((HOST,PORT))

print("Conectado com sucesso!\nEndereço do servidor: " + str(HOST) + "\nPorta: " + str(PORT) + "\n\nLista de comandos: \nsoma a b: Retorna soma de a+b \nraiz_quadrada a\: Retorna a raiz quadrada de a\n'exit: Encerra a conexão\n")

while True:
	message = input("Insira o comando: ")
	while not message:
		print("Mensagem inválida.\n")
		message = input("Insira o comando: ")
	byte_msg = message.encode('utf-8')
	tcp_client_socket.send(byte_msg)
	data = tcp_client_socket.recv(2048)
	data = data.decode('utf-8')
	print(data + "\n")
	if message == 'exit':
		break
tcp_client_socket.close()
