from flask import Flask, render_template, request
from threading import Thread
import robot
import socket

# Setup thread per controllo robot
threadRobot = Thread(target=robot.start)
threadRobot.start()

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
@app.route("/set-direzione")
def set_direzione():
	direzione = request.args.get('direzione', 0, type=str)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('localhost', robot.PORTA))
	s.sendall(direzione.encode())
	s.close()
	return ('', 204)

if(__name__ == '__main__'):
	app.run(host='0.0.0.0')
