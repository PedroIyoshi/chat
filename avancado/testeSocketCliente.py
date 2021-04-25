import socket;

host = 'localhost'
port = 6545
nick = 'primeiro'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s = socket.create_connection((host, port))
s.connect((host, port))

while True:
	mensagem = input();
	s.sendall(str.encode(mensagem))
