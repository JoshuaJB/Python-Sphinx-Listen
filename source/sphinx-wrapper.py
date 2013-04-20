#!/usr/bin/env python
import gst
import threading
import gobject
gobject.threads_init()
class backgroundListener(src=alsasrc):
	def __init__(self, src=alsasrc):
		threading.Thread.__init__(self, name='VRecognisionThread')
		self.phrases=[]
	def listen(self, string, event):
		"""Accepts an event to be triggered when a string is found in an utterance
			-event should be a function
			-string should be a string
			Returns ValueError if string is not of type str."""
		try:
			assert str=type(string)
			self.phrases.append([string, event])
		except(AssertionError):
			return ValueError
