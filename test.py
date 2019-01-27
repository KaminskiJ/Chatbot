import string
import re

#string.printable
#'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
#
#string.ascii_letters
#'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#string.ascii_lowercase
#'abcdefghijklmnopqrstuvwxyz'

#line = re.sub('[!@#$]', '', line)

print(string.punctuation)
tekst = 'cwWSsf asf .sgas tak?'

tekst2 = re.sub('[.?!@#$]', '', tekst)
print(tekst2, 'ico')

print(tekst.lower().split())


import sys,time,random

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print(t)