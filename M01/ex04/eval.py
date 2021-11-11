class Evaluator:
	@staticmethod
	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			return (-1)
		result = zip(words, coefs)
		result_list = list(result)
		mul = 0
		for i in result_list:
			mul = mul + (len(i[0]) * i[1])
		return mul


	@staticmethod
	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			return (-1)
		mul = 0
		for word in enumerate(words):
			for coef in enumerate(coefs):
				if word[0] == coef[0]:
					mul = mul + (len(word[1]) * coef[1])
		return mul
