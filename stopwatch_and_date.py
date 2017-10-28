# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:01:48 2017

@author: choip
"""

#import time
#
#print ('Press enter to begin, afterwards, press enter to click the stopwatch. Press Ctrl-C to quit')
#
#input() #press Enter to begin
#
#print ('started')
#
#startTime = time.time()
#lastTime = startTime 
#lapNum = 1
#
#try:
#    while True:
#        input()
#        lapTime = round(time.time()-lastTime,2)
#        totalTime = round(time.time()- startTime,2)
#        print ('Lap {}: {} {}'.format(lapNum,totalTime,lapTime))
#        lapNum += 1
#        lastTime = time.time()
#except KeyboardInterrupt:
#    print ('\nDone.')

import datetime
import time 

print (datetime.datetime.now())
dt = datetime.datetime(2015,10,21,16,29,0)
print (dt.year,dt.month,dt.day)
print (dt.hour, dt.minute, dt.second)

print (datetime.datetime.fromtimestamp(100000))
print (datetime.datetime.fromtimestamp(time.time()))

halloween2015 = datetime.datetime(2015,10,31,0,0,0)
newyears2016 = datetime.datetime(2016,1,1,0,0,0)

print (newyears2016 > halloween2015)

delta = datetime.timedelta(days = 11, hours = 10, minutes = 9, seconds = 8)

print (delta.total_seconds())
print (delta.days,delta.seconds,delta.microseconds)
print (str(delta))

dt = datetime.datetime.now()
seconds = datetime.timedelta(seconds = 300000000)

print (dt + seconds)

d0 = datetime.date(2008,8,18)
d1 = datetime.date(2008,9,26)
delta = d1 - d0
print (delta)

#pausing until certain day
#halloween2016 = datetime.datetime(2016,10,31,0,0,0)
#while datetime.datetime.now() < halloween2016:
    #time.sleep()
    
oct21st = datetime.datetime(2015,10,21,16,29,0)
print (oct21st.strftime('%Y/%m/%d/ %H: %M: %S'))

print (oct21st.strftime('%I: %M %p'))
print (oct21st.strftime('%B of %y'))

print (datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
print (datetime.datetime.strptime('October of 15','%B of %y'))

import threading

print('start')

def takenap():
    time.sleep(5)
    print ('wake up')

threadobj = threading.Thread(target = takenap)
#not takenap()
#print done is ran wile threadobj.start is run.
#hence, done is printed first than wake up

threadobj.start()

print ('done')