"""Map the function to all elements of the iterable.
Args:
function_to_apply: a function taking an iterable.
iterable: an iterable object (list, tuple, iterator).
Returns:
An iterable.
None if the iterable can not be used by the function.
"""

def ft_map(function_to_apply, iterable):
	try:
		function_to_apply(iterable[0])
	except:
		return None
	res = []
	for count, el in enumerate(iterable):
		try:
			res.append(function_to_apply(el))
		except ValueError:
			return None
	return res
