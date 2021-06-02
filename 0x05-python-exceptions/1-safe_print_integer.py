#!/usr/bin/python3
def safe_print_integer(value):
	""" this is a comment """
	try:
		print("{:d}".format(value))
		return True
	except Exception:
		return False
