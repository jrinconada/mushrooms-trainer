from urllib.request import urlopen, Request
import requests
import os

def get_page(name):
    base_url = 'http://www.mushroom.world/show?n='
    url = base_url + name[0] + '-' + name[1]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    request = Request(url, headers=headers)
    response = urlopen(request)
    webContent = response.read()
    print(webContent.decode("utf-8"))

def download_image(name):
    base_url = 'http://www.mushroom.world/data/fungi/'
    folder = 'training_data/' + name[0].lower() + '_' + name[1].lower() + '/'
    if not os.path.exists(folder):
        os.makedirs(folder)
    for i in range(1,7):
        image = name[0] + name[1] + str(i) + '.JPG'
        url = base_url + image
        data = requests.get(url).content
        with open(folder + image, 'wb') as handler:
            handler.write(data)

def read_mushroom_list(name):
    # Read the names of the mushrooms from a file
    with open(name, 'r') as file:
        names = file.read()

    # Every line is a name with this format: Amanita muscaria (Fly Amanita)
    # We want to end up with a list of only tuples of scientific names: 
    # [...(Amanita, muscaria), (Amanita, pantherina)...]
    names = names.split('\n')
    scientific_names = []
    for name in names:
        words = name.split(' ')
        scientific_names.append((words[0], words[1]))

    return scientific_names

def download_all(scientific_names):
    # Dowload all the images
    for mushroom in scientific_names:
        download_image(mushroom)

names = read_mushroom_list('mushroom-list.txt')

# To get an specific mushroom page
# get_page('http://www.mushroom.world/show?n=Agaricus-arvensis')
