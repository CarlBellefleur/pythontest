import time

"""
Carl Bellefleur
cb07d
2/19/16
blahhhhhhhh
"""

def t_decorator(blah):
	def t_wrapper():
		timebeg = time.time()
		blah()
		timeend = time.time()
		return "Time to execute function(s): " + str(timeend - timebeg)
	return t_wrapper
