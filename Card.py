

class Card(object):

	def __init__(self, name, stat1, stat2, stat3):
		self.name = name
		self.stat1 = stat1
		self.stat2 = stat2
		self.stat3 = stat3

	def __repr__(self):
		string = ""
		string += self.name + "\n" + self.stat1 + "\n" + self.stat2 + "\n" + self.stat3
		return string