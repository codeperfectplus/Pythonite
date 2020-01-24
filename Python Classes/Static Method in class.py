""" Static methods are methods within a class that have no access to anything else in the class (no self keyword or cls keyword). They cannot change or look at any object attributes or call other methods within the class. They can be thought of as a special kind of function that sits inside of the class. When we create a static method we must use something called a decorator. The decorator for a static method is "@staticmethod" """

class Myclass:
    def __init__(self):
        self.x = x 

    @staticmethod
    def staticmethod():
        return "I Am A Staic Method"
# Staticmethod does not require self PARAMETER