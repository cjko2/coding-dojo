class MathDojo(object):

	def __init__(self):
		self.result = 0

	def add(self, *varargs):
		for n in varargs:
			if isinstance(n, list) or isinstance(n, tuple):
				for i in n:
					self.result += i
			else:
				self.result += n
		return self

	def subtract(self, *varargs):
		for n in varargs:
			if isinstance(n, list) or isinstance(n, tuple):
				for i in n:
					self.result -= i
			else:
				self.result -= n
		return self


print MathDojo().add(2).add(2,5).subtract(3,2).result
print MathDojo().add([1],3,4).add((3, 5, 7, 8), [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result