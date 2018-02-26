jay = [1,2,3,4,5,-1,-2,-3,-4,-5]
total = 0
j = len(jay) -1
while jay[j] < 0:
	total += jay[j]
	jay -= total
print(total)