import json
input_file = open('input_file.dat','r')
fb = input_file.read()
input_file.close()
my_set = set()
new_dict = {}
for word in fb.split():
    #count the number of words
    numer_of_words = fb.count(word)
    #add words as key and number of words as value
    new_dict[word] = numer_of_words
    keys = new_dict.keys()
for key in keys:
    print(key,new_dict[key])

new_output = open('new_output.dat','w')
new_output.write(json.dumps(new_dict))
new_output.close()

