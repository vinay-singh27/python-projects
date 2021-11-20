
def factorial(n):
	"""
	Return the Factorial of a number using recursion
	Parameters:
	n -- Number to get factorial of
	"""
	if not n:
		return 1
	return n*factorial(n-1)

print(factorial(5))