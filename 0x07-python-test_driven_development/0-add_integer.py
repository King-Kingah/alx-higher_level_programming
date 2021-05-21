#!usr/bin/python3
"""
This is the "Add Integer" module.

This module supplies one function, add_integer(), which adds together 2 
int or float types and returns an int.
"""

def add_integer(a, b):
	"""Return the sum of 2 integers or floats an an int.
	Otherwise raise a TypeError for given incorrect argument type.
	"""
	h = list(map(lambda x: isinstance(x, (int, float)), [a, b]))
	
	if all(h):
		return int(a) + int(b)

	for x, y in list(zip(h, ['a', 'b'])):
		if not x;
			raise TypeError("{} must e an integer".format(y))
