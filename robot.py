import gpiozero
import socket
import time

PORTA = 5001

pwma = pwmb = robot = None

def setup():
	global robot, pwma, pwmb
	robot = gpiozero.Robot((17,4),(22,27), pwm=False)
	robot.stop()
	pwma = gpiozero.PWMOutputDevice(2, frequency=25000, initial_value=0.5)
	pwmb = gpiozero.PWMOutputDevice(3, frequency=25000, initial_value=0.5)

def start():
	if(robot == None):
		setup()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('0.0.0.0', PORTA))
	s.listen(0)
	while True:
		conn, addr = s.accept()
		direzione = conn.recv(1024)
		direzione = int(direzione.decode())
		print(direzione)
		if(direzione == 0):
			robot.stop()
		elif(direzione == 1):
			robot.forward()
		elif(direzione == 2):
			robot.backward()
		elif(direzione == 3):
			robot.right()
		elif(direzione == 4):
			robot.left()
		else:
			print('Nessuna direzione')
