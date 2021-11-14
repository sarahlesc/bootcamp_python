"""Apply function of two arguments cumulatively.
Args:
function_to_apply: a function taking an iterable.
iterable: an iterable object (list, tuple, iterator).
Returns:
A value, of same type of elements in the iterable parameter.
None if the iterable can not be used by the function.
"""

def ft_reduce(function_to_apply, iterable):
	try:
		function_to_apply(iterable[0], iterable[1])
	except:
		if len(iterable) > 2:
			return None
	ret = []
	x = 0
	res = ""
	while x < len(iterable) - 1:
		try:
			res = res + function_to_apply(iterable[x], iterable[x + 1])
		except:
			print("ERROR")
			return None
		x += 2
	if len(iterable) % 2 != 0:
		res = res + iterable[x]
	return res
