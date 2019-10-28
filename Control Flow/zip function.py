'''
this function is helpful to combine similar type iterators
'''


phone =['samsung s10', 'iphone 10']
accessories =['Charger', 'Headphones']

for c, a in zip(phone, accessories):
	print('phone :%s, Accessory Require: %s' %(c, a))