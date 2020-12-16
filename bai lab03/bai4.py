class Greeter(object):
	def __init__(self, name):
		self.name = name
	def greet(self, loud=False):
		if loud:
			print('HELLO, %s!' % self.name.upper())
		else:
			print('Hello, %s' % self.name)