from os import walk
from os.path import dirname, realpath, splitext, join

def update_draft():
    dir_path = join(dirname(realpath(__file__)), 'content')
    for path, _, files in walk(dir_path):
        content_files = [file for file in files if ((splitext(file)[1] == '.md' or splitext(file)[1] == '.html') and splitext(file)[0] != 'blog_template')]
        for file in content_files:
            print(f'undrafting {file}')
            full_path = join(path, file)
            with open(full_path, 'r') as f:
                file_lines = f.readlines()
            for count, line in enumerate(file_lines):
                if 'draft' in line:
                    break
            file_lines[count] = 'draft: false\n'
            with open(full_path, 'w') as f:
                f.writelines(file_lines)
if __name__ == '__main__':
    update_draft()