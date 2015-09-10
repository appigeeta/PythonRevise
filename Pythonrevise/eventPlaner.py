#!usr/bin/python
#general sketch for for organising an event.
class booking:
	def __init__(self,date,time):
		self.date=date
		self.time=time
#printing just to make sure 
		print date
		print time
class place:
	def place_sele(self,indoor,outdoor):
		self.indoor=indoor
		self.outdoor=outdoor

class attendees:
	def att(self,headcount):
		self.headcount=headcount

class food:
	def food_choice(self,veg,nonveg):
		self.veg=veg
		self.nonveg=nonveg

class party_type:
	def type(self,name):
		self.name=name
		print name
#selection from..bday,graduation,anniversary,wedding,company event..etc
	def bday(self,packages,theme,entertainment):
		self.packages=packages
		self.theme=theme
		self.entertainment=entertainment
		self.headcount=headcount
		def packages(self,A,B,C,):
			self.A="only decoration"
			self.B="A+cake+food"
			self.C="B+goodiebags"
		def entertainment(self,ch,mg,ba,fp):
			self.ch="character"
			self.mg="magician"
			self.ba="balloonmaker"
			self.fp="face painting"
def costEstimation(self,attendees):
	print self.attendees()
