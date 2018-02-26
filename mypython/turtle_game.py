import turtle

jay = turtle.Turtle()
def square(length,angle):
	for i in range(4):
		jay.forward(length)
		jay.left(angle)
for i in range(100):
	square(100,90)
	jay.left(10)
squares(100, 90)

class Rational:
    def __init__(self, num, denom):
        self =
        self.numerator = num
        self.denominator = denom

print(self.numerator)

from datetime import date
l_date = date(1995, 9, 7)
f_date = date(2018, 2, 3)
jay = f_date - l_date
print(jay.days)

#from IPython.display import clear_output
def display_board(board):
	clear_output()
	print('    |      |     ')
	print('----|------|-----')
	print('    |      |     ')

display_board([])
