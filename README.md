# raspberry-robot
Robot comandato da un Raspberry in python attraverso interfaccia web

## Schema dei collegamenti
Il programma è stato sviluppato su un Raspberry 4 quindi lo schema dei pin potrebbe cambiare.
Per controllare i motori ho utilizzato una breakout board con il chip TB6612FNG
Di seguito i collegamenti dei pin

Rpi4	->	IC  
GPIO2	->	pwmA  
GPIO3	->	pwmB  
GPIO4	->	aIN1  
GPIO17	->	aIN2  
GPIO27	->	bIN1  
GPIO22	->	bIN2  
GND		->	GND  
5v		->	VCC  
GND		->	STBY  

## Istruzioni
Prima di utilizzare il programma bisogna installare il pacchetto **pigpio**, installabile con: `sudo apt update && sudo apt install pigpio -y`

Dopo di che scaricate il codice e assicuratevi di installare le dipendenze di Python con: `pip install -r requirements.txt`

Prima di avviare il programma bisogna avviare il servizio pigpiod con `sudo service pigpiod start` oppure avviarlo al boot con `sudo systemctl enable pigpiod`

Poi basterà avviare il tutto con `python3 app.py`

Il programma avvierà un server Flask in ascolto sulla porta 5000, recatevi all'indirizzo ip del vostro raspberry e avrete i due joystick con cui comandare il robot.
