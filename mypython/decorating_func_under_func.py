def helloo(name = "jay"):
    print "the hello function has been exicuted"

    def greet():
        return "\t this is greet"

    def welcome():
        return "\t welcome to the world"

    print(greet())
    print(welcome())
    print "now we are back inside the hello() function"

print(helloo())


def hello(name="jose"):
    def greet():
        return "\t this is another greet "
    def welcome():
        return "this is an another welcome in hello func"
    if name == "jose":
        return greet
    else:
        return welcome

x = hello()()
print(x)
