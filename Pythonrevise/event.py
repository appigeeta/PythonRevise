#!/usr/bin/python
class event:

	def __init__ (self):
		print"event details"
	def attd(self,attendees):
		self.attendees=attendees
	def ch(self,chairs):
		self.chairs=chairs
	def tab(self,tables):
		self.tables=tables
	def f(self,food):
		self.food=food

	def event_details(self):
		print self.attendees
		print self.chairs
		print self.tables
		print self.food