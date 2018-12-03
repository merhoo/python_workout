from __future__ import print_function

the_count = [1, 2, 3, 4, 5]
fruit = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


for number in the_count:
    print("This is count %d" % number)

for fruit in fruit:
    print("A fruit of type: %s" % fruit)

for i in change:
    print ("I got %r" % i)

elements = []

for i in range(0, 6):
    print ("Adding %d to the list." % i)
    elements.append(i)

for i in elements:
    print ("Elements was: %d" % i)

beautiful_number = input("tell me a beautiful number. ")
print(beautiful_number)

# end = ":"
for i in "python":
    # print(i + ":")
    print(i, end=":")
print()
