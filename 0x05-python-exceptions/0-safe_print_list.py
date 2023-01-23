#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	count = 0
	if x == 0:
		print("")
		return count
	try:
		for i in range(x):
			print("{}".format(my_list[i]), end="")
			count++
	except Exception as e:
		print("")
	print("")
	return count
	