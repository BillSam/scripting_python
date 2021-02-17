import requests
import hashlib
import sys


def request_api_date(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching : {res.status_code}, check the api')
    return res


# def read_response(response):
#     print(response.text)


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check  password if it exist in API response
    sha1passwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chr, tail = sha1passwd[:5], sha1passwd[5:]
    resp = request_api_date(first5_chr)

    return get_password_leaks_count(resp, tail)


def main(args):
    for password in args:
        cont = pwned_api_check(password)
        if cont:
            print(f'{password} was found {cont} times...')
        else:
            print(f'{password} was not found')
    return 'done'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
