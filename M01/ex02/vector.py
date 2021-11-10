class Vector:
	def __init__(self, dataList):
		if isinstance(dataList, list) == True:
			self.dataList = dataList
			if (isinstance(self.dataList[0], list) == True):
				# CASE OF THE COLUMN
				form = 'column'
			else:
				if (isinstance(self.dataList[0], float) == True):
					# CASE OF THE ROW
					form = 'row'
				else:
					print("Wrong format of the numbers in the vector")
					exit()
		elif isinstance(dataList, int):
			# CASE OF THE SIZE
			self.dataList = [x for x in range(dataList)]
			i = 0
			while i < dataList:
				self.dataList[i] = [i, 0]
				i += 1
			form = 'column'
		elif isinstance(dataList, tuple):
			# CASE OF THE RANGE
			if len(dataList) != 2:
				print("Wrong format of the range")
				exit()
			beginning = dataList[0]
			end = dataList[1]
			self.dataList = [x for x in range(end - beginning)]
			i = 0
			while i < (end - beginning):
				self.dataList[i] = [beginning + i, 0]
				i += 1
			form = 'column'
		else:
			print('Wrong format of the vector.')
			exit()
		if (form == 'column'):
			self.shape = (len(self.dataList), 1)
		else:
			self.shape = (1, len(self.dataList))
		self.values = self.dataList


	def form(self, dataList):
		form = None
		if (isinstance(dataList[0], list) == True):
			form = 'column'
		else:
			form = 'row'
		return form


	def __values__(self):
		print(self.values)


	def __shape__(self):
		print(self.shape)


	def verif(self, datalist1, datalist2):
		if type(datalist1) != type(datalist2):
			print('operation impossible : different type.')
			exit()
		if datalist1.shape[0] != datalist2.shape[0] or datalist1.shape[1] != datalist2.shape[1]:
			print('operation impossible : different shape.')
			exit()
		return

	def __add__(self, new_dataList):
		self.verif(new_dataList, self)
		format = self.form(new_dataList.dataList)
		new_vector = []
		i = 0
		while i < len(new_dataList.dataList):
			if format == 'row':
				new_vector.append(self.dataList[i] + new_dataList.dataList[i])
			else:
				new_vector.append(self.dataList[i][0] + new_dataList.dataList[i][0])
			i += 1
		print(new_vector)
		return Vector(new_vector)

	def __sub__(self, new_dataList):
		self.verif(new_dataList, self)
		format = self.form(new_dataList.dataList)
		new_vector = []
		i = 0
		while i < len(new_dataList.dataList):
			if format == 'row':
				new_vector.append(self.dataList[i] - new_dataList.dataList[i])
			else:
				new_vector.append(self.dataList[i][0] - new_dataList.dataList[i][0])
			i += 1
		print(new_vector)
		return Vector(new_vector)

	def __truediv__(self, new_dataList):


	def __mul__(self, new_dataList):
