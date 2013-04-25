#!/usr/bin/env python
import sphinxwrap
import time
def printNote():
	print "Yes?"
mic=sphinxwrap.backgroundListener()
mic.add("computer", printNote)
mic.add("close", exit)
mic.startListening()
i=6
while(i>0):
	i-=1
	time.sleep(10)
	print 10*i
