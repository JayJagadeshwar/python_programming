class Dog(object):
    spicies = 'mammal'

    def __init__(self, breed, fur, name, dashdash, hustle, rockstar):
        self.breed = breed
        self.fur = fur
        self.name = name
        self.dashdash = dashdash
        self.hustle = hustle
        self.rockstar = rockstar

sam = Dog(breed = 'huskie', name = 'johney', fur = 'rock', dashdash = 'mock', hustle = ' just', rockstar = 'jay')

print(sam.breed, sam.rockstar)
print(sam.name)
print(sam.fur)
print(sam.dashdash)
print(sam.hustle)
print(sam.spicies)
