def elapsed(seconds):
	#This uses the current unix time and assumes the timestamp entered is a total_seconds in unix time as well.
	import time as t
	sign_string = "-" if seconds < 0 else ''
	now = int(t.time())
	elapsed = int(now - int(seconds))
	print elapsed
