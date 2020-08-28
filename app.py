from flask import Flask, render_template
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)

app = Flask(__name__)

@app.route('/on')
def on():
	GPIO.output(18,GPIO.HIGH)
	return render_template('on.html')
	
@app.route('/off')
def off():
	GPIO.output(18,GPIO.LOW)
	return render_template('off.html')






