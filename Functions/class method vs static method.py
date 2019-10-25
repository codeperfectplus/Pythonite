'''
The @class method  decorator in python is inbuilt fuction decorator.
that get evalueted after function.

(1).A class method takes cls as first parameter while a static method needs no specific parameter.
(2).A class method can access or modify class state whilea static method ca't access or modify it.

'''

from datetime import date
class Person(object):
	"""docstring for Person"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	@staticmethod
	def isAdult(age):
		return age >18

Person1 = Person('Alexa',21)
person2 = Person.fromBirthYear('Siri', 1992)

print(Person1.age)
print(person2.age)

print(Person.isAdult(20))
