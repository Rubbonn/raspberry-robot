from flask import Flask, render_template, request
import gpiozero

# Setup robot
robot = gpiozero.Robot((17,4), (22,27), pwm=False)
robot.stop()
pwma = gpiozero.PWMOutputDevice(2, frequency=25000, initial_value=0.5)
pwmb = gpiozero.PWMOutputDevice(3, frequency=25000, initial_value=0.5)

# Setup flask
app = Flask(__name__)

# Homepage con comandi
@app.route("/")
def index():
	return render_template("index.html")

# Impostazione del movimento del robot
@app.route("/set-direzione")
def set_direzione():
	direzione = request.args.get('direzione', 0, type=int)
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
	return ('', 204)

if(__name__ == '__main__'):
	app.run(host='0.0.0.0')
