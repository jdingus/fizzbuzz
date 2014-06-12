import sys

def evenly_divide(numerator,denominator):
	"""Determines if one number is evenly divisible by another and returns true or false"""
	if numerator % denominator==0: 
		return True
	else:
		return False

def print_the_fizz(top=100):
	"""Prints in FizzBuzz language, top is high limit to count to"""
	print "Fizz buzz counting up to "+str(top)
	for i in range(1,top+1):
		if evenly_divide(i,3)==1 and evenly_divide(i,5)==1:
			print 'FizzBuzz'
		elif evenly_divide(i,3)==1:
			print 'Fizz'		
		elif evenly_divide(i,5)==1:
			print 'Buzz'		
		else:
			print str(i)

def main():
	if len(sys.argv)>1: 
		try:
			top=int(sys.argv[1])  # If ran from command line use passed argument for top value
			print_the_fizz(top)
		except ValueError:         # Gives opportunity to raw_input integer, error handling loops until correct input
 			while True:
 				try:
 					print ''
 					top=int(raw_input("Non-integer passed, please re-enter an integer. : "))
 					# break
 					print_the_fizz(top)
 					break
 				except ValueError:
 					print ''
	else:	# If no second arg passed will prompt user for fizzbuzz top count
		while True:
			try:
				top=int(raw_input('How high do you want FizzBuzz to count? : '))
	 			print_the_fizz(top)
	 			break
			except ValueError: # exeption handling will loop until correct input
				print ''
				print 'Non-integer passed, please re-enter an integer.'
				print ''

if __name__ == "__main__":   
	main()