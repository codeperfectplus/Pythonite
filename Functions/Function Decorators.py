def decorate_message(fun): 
  
    # Nested function 
    def addWelcome(site_name): 
        return "Welcome to " + fun(site_name) 
  
    # Decorator returns a function 
    return addWelcome 
  
@decorate_message
def site(site_name): 
    return site_name; 
  

print (site("Python") )

def attach_data(func):
	func.data = 3
	return func

@attach_data
def add (x, y):
	return x + y

print(add(3,5))
print(add.data)