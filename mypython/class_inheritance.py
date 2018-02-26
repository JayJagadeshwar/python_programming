class Animal(object):
    def __init__(self):
        print "animal is created"

    def whoAmI(self):
        print "jay"

    def eat(self):
        print "Eating"


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Dog created"

    def whoAmI(self):
        print "dog"

    def bark(self):
        print "woof"

print(Dog())
