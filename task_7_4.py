import os


def dir_stat(folder='./'):
    stat_dict = {
        100: 0,
        1000: 0,
        10000: 0,
        100000: 0,
    }

    for root, _, files in os.walk(folder):
        for file in files:
            match len(str(os.stat(os.path.join(root, file)).st_size)):
                case 1:
                    stat_dict[100] += 1
                case 2:
                    stat_dict[100] += 1
                case 3:
                    stat_dict[1000] += 1
                case 4:
                    stat_dict[10000] += 1
                case 5:
                    stat_dict[100000] += 1
    return stat_dict


if __name__ == "__main__":
    print(dir_stat('some_data'))
