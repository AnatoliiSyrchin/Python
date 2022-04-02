import os

PROJECT_DICT = {
    'my_project': (
        {'settings': []},
        {'mainapp': [
            {'some_folder': []},
            {'some_folder_2': [
                'some_file_3.bin']},
            'python.bin',
            'some_file.bin']},
        {'adminapp': []},
        {'authapp': []}
    )
}


def dir_creator(dirs_tree, folder=""):
    for key in dirs_tree:
        temp_path = os.path.join(folder, key)
        try:
            os.mkdir(temp_path)
        except FileExistsError:
            print(f'{temp_path} already exists')
        for value in (dirs_tree[key]):
            if type(value) is dict:
                dir_creator(value, temp_path)
            else:
                try:
                    open(os.path.join(temp_path, value), "x")
                except FileExistsError:
                    print(f'{os.path.join(temp_path, value)} already exists')


if __name__ == "__main__":
    dir_creator(PROJECT_DICT)
