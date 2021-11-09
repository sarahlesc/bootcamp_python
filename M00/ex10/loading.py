import time
import random
import sys


def ft_progress(lst):
	num = 0
	start = time.time()
	for num in lst:
		num +=1
		yield num
		end = time.time()
		elapsed_time = end - start
		max_lst = max(lst)
		era = int(num / max_lst * 100)
		eta = f"ETA: {abs(elapsed_time / num * (max_lst - num)):.2f}s"
		bar = int(25 * era / 100)
		if era >= 100:
			eta = 'FINISHED'
		sys.stdout.write(f"{eta:15}	[{era:3}%] [{('=' * (bar - 1) + '>'):25}]	{num:4}/{max_lst + 1}	| elapsed time {elapsed_time:5.2f}s\r")
		sys.stdout.flush()

#listy = range(3333)
#ret = 0
#for elem in ft_progress(listy):
#	ret += elem
#	time.sleep(0.005)
#print()
#print(ret)
