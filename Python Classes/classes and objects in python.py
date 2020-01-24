'''
@author : CodePerfectPlus
@python
'''


class dog():
    def __init__(self, name, age):
        self.name= name
        self.age = age
    
    def speak(self):
        print(f"I am {self.name} and my age is {self.age}.")

one = dog("Tuktuk", 12)
two = dog("Tyson",4)
three = dog("Mike", 5)

one.speak()
two.speak()
three.speak()


    