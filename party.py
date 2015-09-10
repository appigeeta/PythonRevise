# event planner 
#!/usr/bin/python
class party_planning:

	def __init__(self,date,time):
		self.date=date
		self.time=time

	def att(self,headcount):
		self.headcount=headcount

	def place_sele(self,place):
		self.place=place

	def food(self,food_choice):
		self.food_choice=food_choice

	def type(self,partyName):
		self.partyName=partyName


	def party_details(self):
		print"Its a :" + self.partyName
		print" Party is on:" +self.date
		
		print "Venue" +self.place
		print "time:" +self.time
		print "Number of guests:" +self.headcount
		print "Food served:" +self.food_choice
		