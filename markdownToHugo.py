import sys
from filecmp import cmp
from os import system, path, remove
import time
from text_to_Hugo import convert
# goal: run python script with name of a markdown file passed as command line argument
# python script takes that name, runs hugo new [name]
# python script then reads that file, takes the information, and appends to that file the converted html fo the markdown

markdown_file = sys.argv[1]
file_name = markdown_file.split('.')[0]

new_file = convert(markdown_file)
new_file_path = f'content/articles/{file_name}.html'

if path.exists(new_file_path):
    with open(new_file_path, 'r') as f:
        next(f)
        line = f.readline()
        # advances the pointer through the front matter of the hugo file, which will not be present in the new file yet
        while line != '---\n':
            line = f.readline()
        line = f.readline()
        # advances the pointer until the start of the html content
        while line == '\n':
            line = f.readline()
        # because the pointer advances to and reads the first line of html content, this is added back to the front
        old_file = ''.join([line] + f.readlines())
        # if the files match, no reason to remake it
        if new_file == old_file:
            print('no change detected')
            quit()
    remove(new_file_path)


system(f'hugo new articles/{file_name}.html')

# timeout = 10
# trys = 0
# while not path.exists(new_file_path) and trys < timeout:
#     time.sleep(0.1)
#     trys +=1

with open(new_file_path, 'a') as f:
    f.write(new_file)

