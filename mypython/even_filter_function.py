def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False
list = range(1,100)
#filtering evens with the given numbers that are contain in range

print(filter(even_check,list))
