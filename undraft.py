from os import walk, system
from os.path import dirname, realpath, splitext, join

def update():
    from markdownToHugo import convert_file
    dir_path = join(dirname(realpath(__file__)), 'content')
    for path, _, files in walk(dir_path):
        content_files = [file for file in files if ((splitext(file)[1] == '.md' or splitext(file)[1] == '.html') and splitext(file)[0] != 'blog_template')]
        for file in content_files:
            print(f'undrafting {file}')
            full_path = join(path, file)
            system(f'hugo undraft {full_path}')

if __name__ == '__main__':
    update()