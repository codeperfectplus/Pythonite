'''
@author : CodePerfectPlus
@Topic  : Args And Kwargs in Python
'''

def student(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['Math', 'Science', 'History']
info = {'name' :'Deepak', 'age' :22}
student(*courses,**info)