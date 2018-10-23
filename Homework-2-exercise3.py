class Udacian:
	"""docstring for Udacian"""
	def __init__(self, name,city,enrollment,nanodegree,status):
		
		self.name = name
		self.city = city
		self.enrollment = enrollment
		self.nanodegree = nanodegree
		self.status = status

	def print_udacian(self):

		print(self.name + " is " + self.enrollment + " in " + self.city + " stading " + self.nanodegree 
			+ " in Sun pm with Ms.Elham , she is " + self.status)

p1=	Udacian("Kalthom","Makkah","enrolled","FSND","ontrack")
p1.print_udacian()	
		
