import sys

if len(sys.argv)>1: # If second arg passed will use this as fizzbuzz top count
	try:
		top=int(sys.argv[1])   # argument passed must be able to be converted into an integer or exception handling
	except ValueError:         # Gives opportunity to raw_input integer, error handling loops until correct input
		while True:
			try:
				print ''
				top=int(raw_input("Non-integer passed, please re-enter an integer. : "))
				break
			except ValueError:
				print ''
else:	# If no second arg passed will prompt user for fizzbuzz top count
	while True:
		try:
			top=int(raw_input('How high do you want FizzBuzz to count? : '))
			break
		except ValueError: # exeption handling will loop until correct input
			print ''
			print 'Non-integer passed, please re-enter an integer.'
			print ''
print "Fizz buzz counting up to "+str(top)
for i in range(1,top+1):
	if i % 3 == 0 and i % 5 == 0:
		print 'FizzBuzz'
	elif i % 3 == 0:
		print 'Fizz'
	elif i % 5 == 0:
		print 'Buzz'
	else: 
		print i