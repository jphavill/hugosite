from os import system
from updateContent import update

if __name__ == '__main__':
    update()
    system(f'hugo server -D')
