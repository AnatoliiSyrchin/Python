import re


def nginx_log(log_line):
    re_logs = re.compile(
        r'^((?:[\w\d]{,4}[\.:])+[\w\d]{,4})\b.*\[(.*)\]\s+\"([A-Za-z]+)\b\s+((?:[/\w\d])+)\b.*"\s+(\d+)\s+(\d+)\s+')
    return re.match(re_logs, log_line).groups()


if __name__ == '__main__':
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f, open('nginx_pars.txt', 'w', encoding='utf-8') as f2:
        for line in f:
            print(nginx_log(line), file=f2)
        print("result in file nginx_pars.txt")
