def bigger_guy(num1, num2, num3):
	if num1 > num2: #num1 is greater than return num1
		return num1
	elif num2 > num3: #num2 is greater than return 2
		return num2
	else:              #else return num3
		return num3
def test_bigger_guy():
	assert bigger_guy(1, 2, 4) == 4
	assert bigger_guy(4, 3, 1) == 4
	assert bigger_guy(8,10,5) == 10
	print('your code is correct')

test_bigger_guy()