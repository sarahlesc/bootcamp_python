class Account(object):
	ID_COUNT = 1


	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		Account.ID_COUNT += 1


	def transfer(self, amount):
		self.value += amount


class Bank(object):
	"""The bank"""
	def __init__(self):
		self.account = []


	def add(self, account):
		self.account.append(account)


	def transfer(self, origin, dest, amount):
		success_dest = False
		for account in self.account:
			if origin == account.ID_COUNT or origin == account.name:
				account_from = account
				success_origin = True
			if dest == account.ID_COUNT or dest == account.name:
				account_to = account
				success_dest = True
		if success_dest == False:
			print("One of the account does not exist")
			return
		if amount < 0:
			print("The amount of the transfer is incorrect")
			return
		if check_corruption(account_from) != 0 or check_corruption(account_to) != 0:
			print("transfer impossible : corrupted account")
			return
		account_from.value -= amount
		account_to.value += amount


	def check_corruption(self, account):
		if isinstance(account, Account):
			lst = dir(account)
			lst = list(filter(lambda x : not x.startswith("__"), lst))
			if len(lst) % 2 == 0:
				return 1
			if list(filter(lambda x: x.startswith('b'), lst)):
				return 2
			if not list(filter(lambda x: x.startswith('zip'), lst)) or not list(filter(lambda x: x.startswith('addr'), lst)):
				return 3
			if not hasattr(account, "name") or not hasattr(account, "id") or not hasattr(account, "value"):
				return 4
			return 0


	def fix_account(self, account):
		ret = check_corruption(account)
		if ret != 0:
			if ret == 1:
				account.append("__new__")
			if ret == 2:
				for i in list(filter(lambda x: x.startswith('__b'), lst)):
					account.remove(i)
			if ret == 3:
				for i in list(filter(lambda x: x.startswith('__zip'), lst)):
					account.remove(i)
				for i in list(filter(lambda x: x.startswith('__addr'), lst)):
					account.remove(i)
			if ret == 4:
				account.append("__name__")
				account.append("__id__")
				account.append("__value__")
