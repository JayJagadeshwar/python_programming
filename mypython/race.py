def number_to_the_choice(choice):
	return {'usain': 1, 'me': 2, 'qazi': 3}[choice]
def test_number_to_choice():
	assert number_to_the_choice('usain') == 1
	assert number_to_the_choice('me') == 2
	assert number_to_the_choice('qazi') == 3
	print("good")

def choice_to_the_number(number):
	return {1: 'usain', 2: 'me', 3: 'qazi'}[number]
def test_choice_to_the_number():
	assert choice_to_the_number(1) == 'usain'
	assert choice_to_the_number(2) == 'me'
	assert choice_to_the_number(3) == 'qazi'
	print("your code is correcr")
test_number_to_choice()
test_choice_to_the_number()