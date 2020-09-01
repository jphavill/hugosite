import sys
from os import system, path, remove
from text_to_Hugo import convert
# goal: run python script with name of a markdown file passed as command line argument
# python script takes that name, runs hugo new [name]
# python script then reads that file, takes the information, and appends to that file the converted html fo the markdown

def convert_file(markdown_file):
    file_name = markdown_file.split('.')[0]
    new_file, title = convert(markdown_file)
    new_file_path = f'content/articles/{file_name}.html'
    if checkOldFile(markdown_file, new_file_path, new_file, title, file_name):
        createHtmlFile(file_name, new_file_path, title, new_file)


def checkOldFile(markdown_file, new_file_path, new_file, title, file_name):
    new_file, title = convert(markdown_file)
    new_file_path = f'content/articles/{file_name}.html'
    if path.exists(new_file_path):
        with open(new_file_path, 'r') as f:
            next(f)
            line = f.readline()
            # advances the pointer through the front matter of the hugo file, which will not be present in the new file yet
            while line != '---\n':
                if 'title' in line:
                    old_title = line.split(':')[1].strip().strip('"')
                line = f.readline()
            line = f.readline()
            # advances the pointer until the start of the html content
            while line == '\n':
                line = f.readline()
            # because the pointer advances to and reads the first line of html content, this is added back to the front
            old_file = ''.join([line] + f.readlines())
            # if the files match, no reason to remake it
            if new_file == old_file and title == old_title:
                print('no change detected')
                return False
        remove(new_file_path)
        return True


def createHtmlFile(file_name, new_file_path, title, new_file):
    system(f'hugo new articles/{file_name}.html')

    with open(new_file_path, 'r') as f:
        # reads the first line, the '---' of the frontmatter
        file_lines = f.readlines()
    file_lines[1] = f'title: "{title}"\n'
    with open(new_file_path, 'w') as f:
        f.writelines(file_lines)
    with open(new_file_path, 'a') as f:
        f.write(new_file)

if __name__ == '__main__':
    markdown_file = sys.argv[1]

    convert_file(markdown_file)


#todo make it one command to scan through all md files and check if any need to be updated