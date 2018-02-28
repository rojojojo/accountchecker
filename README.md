# accountchecker
Python script to automate lookups on HaveIBeenPwned.com

You can use this tool to look up a username or password & check if it has been breached. You can also provide a text file with a list of users (one user/account per line).

Dependencies:
requests library

Install this library using the following command:
pip install requests

usage:  
accountchecker.py [-h] [-u USERNAME] [-f FILENAME] [-p PASSWORD]

-h, --help   show this help message and exit
-u USERNAME  Username to be checked
-f FILENAME  Textfile with the list of usernames
-p PASSWORD  The password to be looked up

Example outputs:
1. python accountchecker.py -u root

root: Your account has been pwned
The account 'root' was found in the following breaches:
Battlefield Heroes
Cannabis.com
Forbes
Gawker
hackforums.net
Insanelyi
Stratfor

2. python accountchecker.py -p root
root: Your password was found in the repository 11097 times


Feedback welcome!
