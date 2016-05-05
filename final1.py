import urllib2
import time

sensor1 = 100
sensor2 = 200
sensor3 = 200
sensor4 = 200
cycletime = 3
def getUrl(light_status):
    url = 'http://chillar.esy.es/light1' + '.php?light=' + light_status
    return url
def sequence(count1,count2,count3,count4):
    # getUrl(1,1)
    response = urllib2.urlopen(getUrl("0111"))
    # response = urllib2.urlopen(getUrl(2,1))
    # response = urllib2.urlopen(getUrl(3,1))
    # response = urllib2.urlopen(getUrl(4,1))
    print 'sleeping ', count1*cycletime
    time.sleep(count1*cycletime)
    response = urllib2.urlopen(getUrl("1011"))
    # response = urllib2.urlopen(getUrl(2,0))
    print 'sleeping ', count2*cycletime
    time.sleep(count2*cycletime)
    response = urllib2.urlopen(getUrl("1101"))
    # response = urllib2.urlopen(getUrl(3,0))
    print 'sleeping ', count3*cycletime
    time.sleep(count3*cycletime)
    response = urllib2.urlopen(getUrl("1110"))
    # response = urllib2.urlopen(getUrl(4,0))
    print 'sleeping ', count4*cycletime
    time.sleep(count4*cycletime)
    print 'done successfully'

while True:
    count1=sensor1/100
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
    sequence(count1,count2,count3,count4)
