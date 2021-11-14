"""Filter the result of function apply to all elements of the iterable.
Args:
function_to_apply: a function taking an iterable.
iterable: an iterable object (list, tuple, iterator).
Returns:
An iterable.
None if the iterable can not be used by the function.
"""

def ft_filter(function_to_apply, iterable):
	try:
		function_to_apply(iterable[0])
	except:
		return None
	res = []
	try:
		for el in iterable:
			if function_to_apply(el):
				res.append(el)
		return res
	except ValueError:
		print('ERROR')
		return None
