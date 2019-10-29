class counter:
	def __init__(self, start, end):
		self.num = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(slef):
		if self.num > self.end:
			raise StopIteration
		else:
			self.num += 1
			return self.num - 1

if __name__ = '__main__':
	a, b =2, 5

	c1 = Counter(a, b)
	c2 = Counter(a, b)

	print ("Print the range withot iter()")

	for i in c1:
		print()
