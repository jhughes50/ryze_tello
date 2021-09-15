# Commander for Tello drone
# Jason Hughes

import socket
import threading

class Commander:

	def __init__(self):

		self.computer_ip = '192.168.10.2' 
		self.computer_port = 8889

		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
		self.socket.bind((self.computer_ip, self.computer_port))

		self.receive_thread = threading.Thread(target=self._receive_thread)
		self.receive_thread.daemon = True
		self.receive_thread.start()

		self.drone_ip = '192.168.10.1'
		self.drone_port = 8889

		self.drone_address = (self.drone_ip, self.drone_port)

		self.send_command('command')

	def send_command(self, command):
		
		self.socket.sendto(command.encode('utf-8'), self.drone_address)
		
	def _receive_thread(self):

		while True:
			try:
				self.response, ip = self.socket.recvfrom(1024)
			except (socket.error, exc):
				print ('Exception socket.error: %s' % exc)
	
	def take_off(self):

		self.send_command('takeoff')
	
	def land(self):
		
		self.send_command('land')

	def forward(self, x):

		self.send_command('forward '+str(x))

	def emergency_stop(self):
	
		self.send_command('emergency')

	def up(self, x):
		
		self.send_command('up '+str(x))

	def down(self, x):

		self.send_command('down '+str(x))

	def right(self, x):

		self.send_command('right '+str(x))

	def left(self, x):

		self.send_command('left '+str(x))

	def back(self, x):

		self.send_command('back '+str(x))

	def cw(self, theta):
		# Rotate clockwise theta degrees
		self.send_command('cw '+str(x))

	def ccw(self, theta):
		# Rotate counter clockwise theta degrees
		self.send_command('ccw '+str(x))

	def flip(self, direction):
		# flips ones direction
		# enter l, r, f or b
		self.send_command('flip '+str(direction))

	def set_3Axis_speed(self, x, y, z, speed):
		#go to x, y, z at "speed"
		self.send_command('go '+str(x)+' '+str(y)+' '+str(z)+' '+str(speed))


