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

# Colors? Bold? ANSI escape sequences: \x1b[A;B;C where A = style, B = Text, C = Background
#   A) 1: bold, 2: faint, 3: italic, 4: underline, 5: blink, 6: fast blink, 7: reverse, 8: hide, 9: strikethrough
#   B/C) black(30/40), red(31,41), green2, yellow3, blue4, magenta5, cyan6, white7
# \x1b[0m resets to default.
print('\x1b[1;37;40m' + "This is only a test." + '\x1b[1;30;40m' + "This is only a test." + '\x1b[0m')
print('\x1b[2;37;41m' + "This is only a test." + '\x1b[2;31;40m' + "This is only a test." + '\x1b[0m')
print('\x1b[3;37;42m' + "This is only a test." + '\x1b[3;32;40m' + "This is only a test." + '\x1b[0m')
print('\x1b[4;37;43m' + "This is only a test." + '\x1b[4;33;40m' + "This is only a test." + '\x1b[0m')
print('\x1b[5;37;44m' + "This is only a test." + '\x1b[5;34;40m' + "This is only a test." + '\x1b[0m')
print('\x1b[6;37;45m' + "This is only a test." + '\x1b[6;35;40m' + "This is only a test." + '\x1b[0m')
print('\x1b[7;37;46m' + "This is only a test." + '\x1b[7;36;40m' + "This is only a test." + '\x1b[0m')
print('\x1b[8;37;40m' + "This is only a test." + '\x1b[8;37;40m' + "This is only a test." + '\x1b[0m')
print('\x1b[9;37;40m' + "This is only a test." + '\x1b[9;37;40m' + "This is only a test." + '\x1b[0m')
