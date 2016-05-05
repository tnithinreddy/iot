import urllib2
import time
import datetime
import thread
import RPi.GPIO as GPIO

sensor1 = 100
sensor2 = 200
sensor3 = 400
sensor4 = 500
cycletime = 1

num = 7
inp = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inp, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(num, GPIO.OUT)


def getUrl(light_status):
    url = 'http://chillar.esy.es/light1' + '.php?light=' + light_status
    return url
def sequence(count1,count2,count3,count4):
    response = urllib2.urlopen(getUrl("0111"))

    print 'sleeping ', count1*cycletime
    time.sleep(count1*cycletime)
    response = urllib2.urlopen(getUrl("1011"))

    print 'sleeping ', count2*cycletime
    time.sleep(count2*cycletime)
    response = urllib2.urlopen(getUrl("1101"))

    print 'sleeping ', count3*cycletime
    time.sleep(count3*cycletime)
    response = urllib2.urlopen(getUrl("1110"))

    print 'sleeping ', count4*cycletime
    time.sleep(count4*cycletime)
    print 'done successfully'
def sendDataToServer(desc):
    print desc
    global sensor1
    while True:
        x=datetime.datetime.now()
	hours=x.hour
        minutes=x.minute
        seconds=x.second

        server = 'http://chillar.esy.es/address1.php?count='+str(sensor1)+'&junctionName='+'DAIICT,Gandhinagar'+'&hh='+str(hours)
        server=server+'&mm='+str(minutes)	
        count1=float(sensor1)/100
        print count1
        sensor1=0
        count2=sensor2/100
        count3=sensor3/100
        count4=sensor4/100
        if count1>5:
            count1=5
        if count2>5:
            count2=5
        if count3>5:
            count3=5
        if count4>5:
            count4=5

        print server
 	urllib2.urlopen(server)
	sequence(count1,count2,count3,count4)
def collectSensorData(desc):
    global sensor1
    global sensor2
    global sensor3
    global sensor4
    print desc
    print sensor1
    while True:
        # sensor1 +=1
        # print 'sensor1 = ', sensor1
        # time.sleep(1)
       time.sleep(0.1)
       i=GPIO.input(inp)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             GPIO.output(num, 0)  #Turn OFF LED
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             sensor1 = sensor1+1
             GPIO.output(num, 1)  #Turn ON LED
             time.sleep(0.1)
try:
 thread.start_new_thread( sendDataToServer, ("thread for server communication",))
 thread.start_new_thread( collectSensorData, ("thread for collecting data communication",))
except:
   print "Error: unable to start thread"

while 1:
    pass
