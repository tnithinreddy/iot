import RPi.GPIO as GPIO
import urllib2
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
true = 1
while(true):
                time.sleep(0.5)
                try:
                        response = urllib2.urlopen('http://www.chillar.esy.es/lighttxt1.php')
                        status = response.read()
                except urllib2.HTTPError, e:
                                        print e.code

                except urllib2.URLError, e:
                                        print e.args

                print status,"light"
                print status[0],"light1"
                print status[1],"light2"
                print status[2],"light3"
                print status[3],"light4"
                if status[0]=='0':
                                GPIO.output(15,GPIO.HIGH)
                elif status[0]=='1':
                                GPIO.output(15,GPIO.LOW)

                if status[1]=='0':
                                GPIO.output(19,GPIO.HIGH)
                                
                elif status[1]=='1':
                                GPIO.output(19,GPIO.LOW)

                if status[2]=='0':
                                GPIO.output(21,GPIO.HIGH)
                elif status[2]=='1':
                                GPIO.output(21,GPIO.LOW)


                if status[3]=='0':
                                GPIO.output(23,GPIO.HIGH)
                elif status[3]=='1':
                                GPIO.output(23,GPIO.LOW)

GPIO.cleanup()
