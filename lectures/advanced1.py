# Describe what is going on in each line below.
# Say how it relates to something we've already learned.
# Come up with an example of where it can be useful.
# Try extending it even further:
#   for example, see if you can insert a scope into any of the single lines below.
# Try things out in PythonAnywhere.
# Report your findings in the chat window!

import os

os.system("cls" if os.name == 'nt' else "clear")

a = xrange(100)

b = [2*i for i in a]

def get_func(func_name):
	def fibonacci(n):
		a = 0
		b = 1
		x = 0
		c = 1
		while (x < n):
			a = b
			b = c
			c = a+b
			x += 1
		return c

	def sum3(n):
		total = 0
		for i in range(0, 3*n, 3):
			total += i
		return total
		a = 0
		b = 1
		x = 0
		c = 1
		while (x < n):
			a = b
			b = c
			c = a+b
			x += 1
		return c

	if (func_name =="fibonacci"):
		return fibonacci
	elif (func_name == "sum3"):
		return sum3
	else:
		print "Invalid string"
		return None

b = get_func("fibonacci")(10)
print(b)
c = get_func("sum3")(10)
print(c)