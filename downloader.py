import requests

# Read the names of the mushrooms from a file
with open('mushroom-list.txt', 'r') as file:
    names = file.read()

# Every line is a name with this format: Amanita muscaria (Fly Amanita)
# We want to end up with a list of only tuples of scientific names: 
# [...(Amanita, muscaria), (Amanita, pantherina)...]
names = names.split('\n')
scientific_names = []
for name in names:
    words = name.split(' ')
    scientific_names.append((words[0], words[1]))

