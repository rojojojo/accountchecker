#! python3
# Author: rojojojo (Rohan)
# accountchecker.py - Python script to automate lookups on HaveIBeenPwned.com

import requests
import time
import argparse
import re

parser = argparse.ArgumentParser(description="Python script to automate lookups on HaveIBeenPwned. You can use this "
                                             "tool to look up a username or password & check if it has been breached. "
                                             "You can also provide a text file with a list of users (one per line). "
                                             "Enjoy!")
parser.add_argument("-u", dest='username', help='Username to be checked')
parser.add_argument("-f", dest='filename', help="Textfile with the list of usernames")
parser.add_argument("-p", dest='password', help="The password to be looked up")
args = parser.parse_args()

username = str(args.username)
filename = str(args.filename)
password = str(args.password)


def breachusercheck(user_name):
    res = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/' + user_name)
    if res.status_code == 200:
        print(user_name + ': Your account has been pwned')
        text = res.text
        nameregex = re.compile(r'"Title":"(.*?)"')              # Regex to check the pattern for title in the response
        mo = nameregex.findall(text)
        print('The account \'%s\' was found in the following breaches:' % user_name)
        for i in mo:
            print(i)
    elif res.status_code == 400:
        print(user_name + ': Bad request — the account does not comply with an acceptable format (i.e. it\'s an '
                          'empty string)')
    elif res.status_code == 403:
        print(user_name + ': Forbidden — no user agent has been specified in the request')
    elif res.status_code == 404:
        print(user_name + ': Not found — the account could not be found and has therefore not been pwned')
    elif res.status_code == 429:
        print(user_name + ': Too many requests — the rate limit has been exceeded')


def breachpasscheck(psw):
    res = requests.get('https://api.pwnedpasswords.com/pwnedpassword/' + psw)
    res.encoding = "utf-8-sig"              # To get the request in the required encoding format
    if res.status_code == 200:
        print(psw + ': Your password was found in the repository %s times' % res.text)
    elif res.status_code == 404:
        print(psw + ': Not found — the password was not found in the Pwned Passwords repository')
    elif res.status_code == 429:
        print(psw + ': Too many requests — the rate limit has been exceeded')


if username != "None":
    time.sleep(2)               # Rate is kept at 2 seconds
    breachusercheck(username)

elif filename != "None":
    temp_file = open(filename)
    for l in temp_file:
        account = l.strip('\n')
        time.sleep(2)
        breachusercheck(account)
elif password != "None":
    time.sleep(2)
    breachpasscheck(password)
