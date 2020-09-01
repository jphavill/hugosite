from os import walk
from os.path import dirname, realpath

home_path = dirname(realpath(__file__))
content_path = home_path + '/content'
for level in walk(content_path):
    print(level)