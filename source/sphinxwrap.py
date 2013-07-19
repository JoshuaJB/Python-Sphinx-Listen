#!/usr/bin/env python
import gst
import threading
import gobject
gobject.threads_init()
class backgroundListener(threading.Thread):
	def __init__(self, src = 'alsasrc'):
		threading.Thread.__init__(self, name='VRecognisionThread')
		self.pipeline = gst.parse_launch(src + ' ! audioconvert ! audioresample  ! vader name = vad auto-threshold = true ! pocketsphinx name = asr ! appsink sync = false name = appsink')
		self.sphinx = self.pipeline.get_by_name('asr')
		self.sphinx.connect('result', self.sphinxResult)
		self.searchTerms = {}
	def add(self, string, event):
		"""Accepts an event to be triggered when a string is found in an utterance
			-event should be a function
			-string of type str
			Rasies ValueError if string is not of type str."""
		try:
			assert str == type(string)
			self.searchTerms[string.lower()] = event
		except(AssertionError):
			raise ValueError
	def remove(self, string):
		"""Removes string from items to listen for.
			-string of type str
			Raises ValueError if string is not of type str.
			Returns True if item was found, False otherwise."""
		try:
			assert str == type(string)
			if (dict.has_key(string)):
				del searchTerms[string]
				return True
			else:
				return False
		except(AssertionError):
			raise ValueError
	def startListening(self):
		"""Starts background listener.
			Begins to searchTerms for specified words in microphone audio stream."""
		self.pipeline.set_state(gst.STATE_PLAYING)
	def stopListening(self):
		"""Pauses background listener.
			Pauses searchTerms for specified words in microphone audio stream."""
		self.pipeline.set_state(gst.STATE_PAUSED)
	def sphinxResult(self, sphinx, text, uttid):
		"Internal function, called when sphinx has a hypothesis"
		for key in self.searchTerms.keys():
			if (key in text):
				self.searchTerms[key]()
