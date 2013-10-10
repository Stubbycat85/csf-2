# Script to simulate a attendance-taking for CSF

import random

# Total number of students
n = 75

# Each student's name is just their number, starting from 1 up to n.
# No student is named 0 (zero).

# Number of iterations of name-writing (phase 1)
k = 5

# The list of lists, where list in names[i] is a list of 5 names
# currently held by student i, some of which may be uninitialized (5)
names = [[0 for x in xrange(k)] for x in xrange(n)]

# Iterate for k rounds of name-taking
for i in xrange(5):
	# Randomly permute the names
	
	# Create a copy of the roster
	names_left = range(n)
	# Create a new list with the names in a random order
	# by starting empty, and then pulling a random index from the copy
	# until the copy is empty
	new_order = []
	
	for j in xrange(n):
		random_index = random.randint(0, len(names_left)-1)
		random_pulled = names_left.pop(random_index)
		new_order.append(random_pulled)
	
	print str(new_order)
	
	# Permute the name lists
	temp = names[new_order[0]]
	for j in xrange(0,n-1):
		names[new_order[j]] = names[new_order[j+1]]
		