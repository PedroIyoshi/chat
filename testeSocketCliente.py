import socket;

host = 'https://frosty-jang-08e2c1.netlify.app/'
port = 14430
nick = 'primeiro'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s = socket.create_connection((host, port))
s.connect((host, port))

while True:
	mensagem = input();
	s.sendall(str.encode(mensagem))
