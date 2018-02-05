import socket
import threading
import sys

'''
class Server:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connection = []
		def __init__(self):
				self.sock.bind(('0.0.0.0', 10000))
				self.sock.listen(1)	
				
		def handler(self, c, a):
				while True:
						data = c.recv(1024)
						for connection in self.connections:
								connection.send(data)
						if not data:
								break
		
		def run(self):
				while True:
						c, a = self.sock.accept()
						cThread = threading.Thread(target=self.handler, args=(c, a))
						cThread.daemon = True
						cThread.start()
						self.connections.append(c)
						print(str(a[0]) + ':' + str(a[1], "connect"))
'''
'''
server = Server()
server.run()
'''		
class Client:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		def sendMsg(self):
				while True:	
						self.sock.send(bytes(input(""), 'utf-8'))
		
		def __init__(self, address):
				self.sock.connect((address, 10000))
				
				iThread = threading.Thread(target=self.sendMsg)
				iThread.daemon = True
				iThread.start()
				
		
				while True:
						data = self.sock.recv(512)
						if not data:
								break
						print(data)		
		
if (len(sys.argv) > 1):	
		client = Client(sys.argv[1])
else:
		print('need to enter server name')		
	
