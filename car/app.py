# -*- coding: utf-8 -*

import RPi.GPIO as GPIO
from flask import Flask, render_template

#設定GPIO相關設定
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT) 
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)


app=Flask(__name__)

#連結到樹梅派的時候會打開網頁
@app.route('/')
def index():
	return render_template('index.html')

#前進
@app.route('/forward',methods=['GET', 'POST'])
def forward():
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(12,GPIO.LOW)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)
        return render_template('index.html')
#每次下完指令，就會再回到首頁，下同

@app.route("/left",methods=['GET', 'POST'])
#左轉
def left():
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(12,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
        return render_template('index.html')

#停止
@app.route("/stop",methods=['GET', 'POST'])
def stop():
	GPIO.output(11,GPIO.LOW)
	GPIO.output(12,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)
        return render_template('index.html')

#右轉
@app.route("/right",methods=['GET', 'POST'])
def right():
	GPIO.output(11,GPIO.LOW)
	GPIO.output(12,GPIO.HIGH)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)
        return render_template('index.html')

#後退
@app.route("/back",methods=['GET', 'POST'])
def back():
	GPIO.output(11,GPIO.LOW)
	GPIO.output(12,GPIO.HIGH)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
