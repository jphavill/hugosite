import sys
from os import system, path, remove
from text_to_Hugo import convert
from json import loads
# goal: run python script with name of a markdown file passed as command line argument
# python script takes that name, runs hugo new [name]
# python script then reads that file, takes the information, and appends to that file the converted html fo the markdown

def convert_file(markdown_file):
    file_name = markdown_file.split('.')[0]
    new_file, title, tags = convert(markdown_file)
    new_file_path = f'content/articles/{file_name}.html'
    if checkOldFile(markdown_file, new_file_path, new_file, title, file_name):
        createHtmlFile(file_name, new_file_path, title, new_file, tags)


def checkOldFile(markdown_file, new_file_path, new_file, title, file_name):
    new_file, title, tags = convert(markdown_file)
    new_file_path = f'content/articles/{file_name}.html'
    if path.exists(new_file_path):
        old_tags = []
        with open(new_file_path, 'r') as f:
            next(f)
            line = f.readline()
            # advances the pointer through the front matter of the hugo file, which will not be present in the new file yet
            while line != '---\n':
                if 'title' in line:
                    old_title = line.split(':')[1].strip().strip('"')
                line = f.readline()
                if 'tags' in line:
                    old_tags = loads(line.split(':')[1])
            line = f.readline()
            # advances the pointer until the start of the html content
            while line == '\n':
                line = f.readline()
            # because the pointer advances to and reads the first line of html content, this is added back to the front
            old_file = ''.join([line] + f.readlines())
            # if the files match, no reason to remake it
            if new_file == old_file and title == old_title and tags == old_tags:
                print('no change detected')
                return False
        remove(new_file_path)
    return True



def createHtmlFile(file_name, new_file_path, title, new_file, tags):
    system(f'hugo new articles/{file_name}.html')
    with open(new_file_path, 'r') as f:
        # reads the first line, the '---' of the frontmatter
        file_lines = f.readlines()
    file_lines[1] = f'title: "{title}"\n'
    for count, line in enumerate(file_lines[2:]):
        if '---' in line:
            break
    file_lines.insert(count+2, f'tags: {tags}\n'.replace("'", '"'))
    with open(new_file_path, 'w') as f:
        f.writelines(file_lines)
    with open(new_file_path, 'a') as f:
        f.write(new_file)

if __name__ == '__main__':
    markdown_file = sys.argv[1]

    convert_file(markdown_file)
