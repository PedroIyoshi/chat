import threading
import socket
import argparse
import os


class Server(threading.Thread):
	def __init__(self, host, port):
		super().__init__()
		self.connections = []
		self.host = host
		self.port = port

	def run(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind((self.host, self.port))
		sock.listen()
		print('Listening at', sock.getsockname())
		while True:
			# Accept new connection
			sc, sockname = sock.accept()
			print('Accepted a new connection from {} to {}'.format(sc.getpeername(), sc.getsockname()))
			# Create new thread
			server_socket = ServerSocket(sc, sockname, self)

			# Start new thread
			server_socket.start()
			# Add thread to active connections
			self.connections.append(server_socket)
			print('Ready to receive messages from', sc.getpeername())

	def broadcast(self, message, source):
		for connection in self.connections:
			# Send to all connected clients except the source client
			if connection.sockname != source:
				connection.send(message)


class ServerSocket(threading.Thread):

	def __init__(self, sc, sockname, server):
		super().__init__()
		self.sc = sc
		self.sockname = sockname
		self.server = server

	def run(self):

		while True:
			message = self.sc.recv(1024).decode('ascii')
			if message:
				print('{} says {!r}'.format(self.sockname, message))
				self.server.broadcast(message, self.sockname)
			else:
				# Client has closed the socket, exit the thread
				print('{} has closed the connection'.format(self.sockname))
				self.sc.close()
				Server.remove_connection(self)
				return

	def send(self, message):
		self.sc.sendall(message.encode('ascii'))

	def exit(server):
		while True:
			ipt = input('')
			if ipt == 'q':
				print('Closing all connections...')
				for connection in server.connections:
					connection.sc.close()
				print('Shutting down the server...')
				os._exit(0)

	if __name__ == '__main__':
		parser = argparse.ArgumentParser(description='Chatroom Server')
		parser.add_argument('-hn', metavar='HOST', default='localhost', help='Interface the server listens at')
		parser.add_argument('-p', metavar='PORT', type=int, default=6545, help='TCP port (default 1060)')
		args = parser.parse_args()
		# Create and start server thread
		server = Server(args.hn, args.p)
		server.start()
		exit = threading.Thread(target=exit, args=(server,))
		exit.start()
















# import socket;
#
# host = socket.gethostbyname('iyoshi.ddns.net')
# host = socket.gethostname()
# port = 6545
# print(host)
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(socket.gethostbyname(socket.gethostname()))
# s = socket.create_server(('', port))
# s.listen()
# conn, addr = s.accept()
# while True:
# 	data = conn.recv(1024)
# 	print(data.decode('UTF-8'))
# 	if not data:
# 		break
# 	conn.sendall(data)
# while True:
# 	f = s.accept()
# 	if not f in conected:
# 		print(f[1])
# 		conected.append(f)
# 	print(f)
# 	for user in f:
# 		data = user[0].recv(1024)
# 		print(data.decode('UTF-8'))

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)


