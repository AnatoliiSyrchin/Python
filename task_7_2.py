import os


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
    import yaml
    from yaml.loader import BaseLoader

    with open('some_file.yaml', 'r') as f:
        dirs = yaml.load(f, Loader=BaseLoader)
    dir_creator(dirs)
    
