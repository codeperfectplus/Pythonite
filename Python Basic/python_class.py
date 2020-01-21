'''
@author : CodePerfectPlus
@Topic  : Python Class 
'''
class Empl(object):
	
	"""docstring for Empl"""
	raise_amount = 1.04
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	def __repr__(self):
		return '{} {}'.format(self.first,self.last)

	def __str__(self):
		return '{} {}'.format(self.first,self.last)

emp_1 = Empl('Deepak', 'Raj', 50)
emp_2 = Empl('Keshav', 'Raj', 3235345)	

#print(emp_1.fullname())
#print(emp_2.fullname())

'''print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
'''
#print(emp_1.__dict__)


print(repr(emp_1))
print(str(emp_1))

 