
"""
Check if your password has been pwned online. With API:
https://haveibeenpwned.com/API/v3

Pwned Passwords overview
Pwned Passwords are more than half a billion passwords which have previously been exposed in data breaches.

Searching by range
In order to protect the value of the source password being searched for, Pwned Passwords also implements a k-Anonymity
model that allows a password to be searched for by partial hash. This allows the first 5 characters of a SHA-1 password
 hash (not case-sensitive) to be passed to the API.

"""

import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    payload = {'timeout' : 12,
                'allow_redirects' : True}
    res = requests.get(url, params=payload)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the api and try again")
    return res

def pawned_api_check(password):
    sha1_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_pass[:5], sha1_pass[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def main(args):
    for password in args:
        print(f"password: {password} is checking")
        leaks_count = pawned_api_check(password)
        if leaks_count:
            print(f"password:{password} was found {leaks_count} times")
        else:
            print(f"{password} was not found!")
    return "Done!"

if __name__ == '__main__':
    passwords = sys.argv[1:]
    print(f"All passswords: {passwords}")
    sys.exit(main(passwords))

