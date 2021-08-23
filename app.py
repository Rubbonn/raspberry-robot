from flask import Flask, render_template, request
import gpiozero
import subprocess
from time import sleep

# Setup servizio pigpiod
print('Tento di avviare il servizio pigpiod...')
servizioAvviato = subprocess.run(['sudo', 'service', 'pigpiod', 'start'])
sleep(2)
if(servizioAvviato.returncode != 0):
	print('Impossibile avviare il servizio pigpiod, hai installato la libreria?')
	exit(1)
print('Servizio avviato!')

# Setup robot
print('Imposto GPIO')
try:
	pigpioFactory = gpiozero.pins.pigpio.PiGPIOFactory()
except:
	print('Impossibile collegarsi al servizio pigpiod, hai installato la libreria e avviato il servizio?')
	exit(1)
robot = gpiozero.Robot((17,4), (22,27), pwm=False)
robot.forward()
pwma = gpiozero.PWMOutputDevice(2, frequency=25000, initial_value=0, pin_factory=pigpioFactory)
pwmb = gpiozero.PWMOutputDevice(3, frequency=25000, initial_value=0, pin_factory=pigpioFactory)
print('GPIO impostati e pronti, avvio il webserver')

# Setup flask
app = Flask(__name__)

# Homepage con comandi
@app.route("/")
def index():
	return render_template("index.html")

# Impostazione del movimento del robot
@app.route("/set-controls")
def set_controls():
	# Prelevo i nuovi parametri
	y = request.args.get('y', 0.0, type=float)
	x = request.args.get('x', 0.0, type=float)
	if(y == 0):
		if(x == 0):
			# Nel caso i joystick siano a 0 fermo il robot
			robot.stop()
		else:
			# Nel caso uso solo il joystick destro, ruoto il robot ad una velocità proporzionale
			if(x > 0):
				pwma.value = pwmb.value = abs(x)
				robot.right()
			elif(x < 0):
				pwma.value = pwmb.value = abs(x)
				robot.left()
	else:
		# Imposto la velocità in base al joystick sinistro
		pwma.value = pwmb.value = abs(y)
		# Nel caso uso anche il joystick destro, rallento un motore per fare una curva
		if(x > 0):
			pwmb.value -= pwmb.value * abs(x)
		elif(x < 0):
			pwma.value -= pwma.value * abs(x)
		# Imposto la direzione in base al joystick sinistro
		if(y > 0):
			robot.forward()
		elif(y < 0):
			robot.backward()
	return ('', 204)

if(__name__ == '__main__'):
	app.run(host='0.0.0.0')
