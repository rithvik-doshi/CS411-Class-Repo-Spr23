import detectlanguage

def getlang(input_string):
	'''
	input_string: can be either a single string or a list of strings
	WARNING: detectlanguagekey needed
	'''
	with open('../.env/detectlanguagekey', 'r') as f:
		detectlanguage.configuration.api_key = f.readline()
	detectlanguage.configuration.secure = True
	out = detectlanguage.detect(input_string)
	# print(out)
	return out


if __name__ == '__main__':
	getlang("hello")
