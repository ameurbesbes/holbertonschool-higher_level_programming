def safe_print_list(my_list=[], x=0):
	try:
		y = 0
		for i in range(0, x):
			print(my_list[i], end="")
			y += 1
	except (TypeError, IndexError):
		pass
	print("")
	return y
