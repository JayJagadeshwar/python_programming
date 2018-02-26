def is_odd(number):
	if number % 2 != 0:
		return True
	else:
		return False

def test_odd():
	assert is_odd(3) == True
	print("jjj")
test_odd()