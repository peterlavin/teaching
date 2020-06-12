

def double(arg):
	print('In double, before: ', arg)
	# This is an assignment, arg is not changed back in the calling code
	# but the local arg is changed
	arg = arg * 2
	print('In double, after:   ', arg)

	
def change(arg):
	print('Before: ', arg)
	arg.append('more data')
	print('After: ', arg)
	
	
if __name__ == '__main__':

	num = 10
	double(num)
	print('Back in main, num is :', num)

	mystr = 'hello '
	double(mystr)
	print('Back in main, mystr is :', mystr)
	
	mynums = [21, 22, 23]
	double(mynums)
	print('Back in main, mynums is :', mynums)
	
	print()

	mynums = [21, 22, 23]
	change(mynums)
	print('Back in main, mynums is :', mynums)
	print()	
	for i in range(95,101):
		print(i)
		
