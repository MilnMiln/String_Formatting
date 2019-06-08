#! /usr/bin/python3

name="John"
age = 30
pi = 3.1415927

print("Hello, %s! I heard you are %d years old! Wow! That's %X in hex!" % (name, age, age)) 
print(pi, "is %.2f, just formatted differently." % pi)

# They say %s is versatile...
mylist = [1, 2, 3]
print("A list: %s, an integer: %s, and a floating point number: %s" % (mylist, age, pi))

# And the exercise: (Splits one line into 3. Easier to look at?)
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is %.2f."
print(format_string % data)
