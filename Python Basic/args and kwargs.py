def student(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['Math', 'Science', 'History']
info = {'name' :'Deepak', 'age' :22}
student(*courses,**info)