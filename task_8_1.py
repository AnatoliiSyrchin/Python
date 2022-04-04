import re


def email_parse(email_address):
    try:
        re_email = re.compile(
            r'(?!.*(\.)\1)^(?P<username>[^.][A-Za-z\d!#$%&"\'*+-/=?^_`{|}~.]+[^.])'
            r'@(?P<domain>[^-][A-Za-z\d-]+[^-].\w{2,3})')
        return re_email.match(email_address).groupdict()
    except AttributeError:
        raise ValueError(f'wrong email: {email_address}')


if __name__ == '__main__':
    print(email_parse('15_45s\'d-d."fd.82@m0-99ail.co'))
