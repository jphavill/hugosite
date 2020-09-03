from os import walk
from os.path import dirname, realpath, splitext

def update():
    from markdownToHugo import convert_file
    dir_path = dirname(realpath(__file__))
    (_, _, files) = next(walk(dir_path))

    markdown_files = [file for file in files if (splitext(file)[1] == '.md' and splitext(file)[0] != 'blog_template')]
    for file in markdown_files:
        print(f'checking {file}', end='\t\t>>>\t')
        convert_file(file)

if __name__ == '__main__':
    update()