import os
import json


def dir_stat(folder='./'):
    stat_dict = {
        100: [0, []],
        1000: [0, []],
        10000: [0, []],
        100000: [0, []]
    }

    for root, _, files in os.walk(folder):
        for file in files:
            ext = file.split('.')[-1]
            match len(str(os.stat(os.path.join(root, file)).st_size)):
                case 1:
                    stat_dict[100][0] += 1
                    if ext not in stat_dict[100][1]:
                        stat_dict[100][1].append(ext)
                case 2:
                    stat_dict[100][0] += 1
                    if ext not in stat_dict[100][1]:
                        stat_dict[100][1].append(ext)
                case 3:
                    stat_dict[1000][0] += 1
                    if ext not in stat_dict[1000][1]:
                        stat_dict[1000][1].append(ext)
                case 4:
                    stat_dict[10000][0] += 1
                    if ext not in stat_dict[10000][1]:
                        stat_dict[10000][1].append(ext)
                case 5:
                    stat_dict[100000][0] += 1
                    if ext not in stat_dict[100000][1]:
                        stat_dict[100000][1].append(ext)

    for key in stat_dict:
        stat_dict[key] = tuple(stat_dict[key])

    with open(f'{folder}_summary.json', 'w', encoding='utf-8') as f:
        json.dump(stat_dict, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    print(dir_stat('some_data'))

