import os
from shutil import copy, SameFileError


def templates_collecting(folder='./'):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.split('.')[-1] == "html" and os.path.split(root)[0] != os.path.join(folder, 'templates'):
                if not os.path.exists(os.path.join(folder, 'templates', os.path.split(root)[1])):
                    os.makedirs(os.path.join(folder, 'templates', os.path.split(root)[1]))
                if not os.path.exists(os.path.join(folder, 'templates', os.path.split(root)[1], file)):
                    copy(os.path.join(root, file), os.path.join(folder, 'templates', os.path.split(root)[1]))
                else:
                    print(f'уже существует {os.path.join(folder, "templates", os.path.split(root)[1], file)}')


if __name__ == "__main__":
    templates_collecting('my_project')
