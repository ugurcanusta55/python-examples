

input_file = open('input_file.dat','r')
fb = input_file.read()
my_set = set()
for word in fb.split():
    my_set.add(word)

print(my_set)

