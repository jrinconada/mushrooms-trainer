from urllib.request import urlopen, Request

def get_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    request = Request(url, headers=headers)
    response = urlopen(request)
    webContent = response.read()
    print(webContent.decode("utf-8"))

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

# To get an specific mushroom: 
# get_page('http://www.mushroom.world/show?n=Agaricus-arvensis')
# http://www.mushroom.world/data/fungi/
