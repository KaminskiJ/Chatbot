import string
import re
from wording import carBrands

#string.printable
#'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
#
#string.ascii_letters
#'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#string.ascii_lowercase
#'abcdefghijklmnopqrstuvwxyz'

#line = re.sub('[!@#$]', '', line)

#print(string.punctuation)
#tekst = 'cwWSsf asf .sgas tak?'
#
#tekst2 = re.sub('[.?!@#$]', '', tekst)
#print(tekst2, 'ico')
#
#print(tekst.lower().split())


lorem = '''

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempor libero iaculis lorem porttitor, a pretium felis eleifend.\n Nulla a consectetur augue. Sed luctus libero ut mauris convallis maximus. Mauris sapien justo, tempus at nunc vel,\n condimentum viverra diam. Mauris egestas lorem vel pulvinar rutrum. Praesent convallis urna sit amet turpis euismod, quis tempor\n lorem tempus. Sed ut odio enim. Donec sagittis tincidunt nisi. Aliquam maximus risus vitae velit tristique rhoncus. \nVestibulum molestie laoreet sem, at convallis neque porta sagittis.

Donec molestie molestie vulputate. Sed placerat facilisis massa, et porttitor lacus mattis ut. Cras a nisl id eros condimentum egestas.\n Morbi malesuada tellus non arcu laoreet facilisis. Curabitur mattis facilisis aliquam. Suspendisse at scelerisque magna. Proin\n in enim quis velit pharetra vehicula. Donec at tellus id ante sollicitudin sodales. Cras imperdiet accumsan elit ac laoreet. '
'''

'''
import sys,time,random

typing_speed = 850 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        #time.sleep(random.random()*2.0/10)
        time.sleep(0.01)
    print(t)

slow_type(lorem)'''

#print(carBrands, sep=', ')


#paczka ktora wyrzuca ratio zestawianych slow.
import difflib
#print(difflib.SequenceMatcher(None, 'hello world', 'hello').ratio())
#result 0.625

brand = ['marka', 'firma', 'nazwa']
brand2 = []
response = 'nazwa'
response2 = ['nazda', 'firma',]
support_list = []
weighted_results = []

#support_list = response2.copy()
'''
user_response_split = ['nazda', 'torota', 'przyklad', 'belkot', 'nic', 'nizan', 'daihztsu', 'honwa', 'koniec stringa']

def similar_word_matcher(wording_list):

    support_list = user_response_split.copy()

    while len(support_list) > 0:

        for result in wording_list:
            ratio = difflib.SequenceMatcher(None, result, support_list[0]).ratio()
            weighted_results.append((result, ratio))

        support_list.pop(0)


    similars = (sorted(weighted_results, key=lambda x: x[1], reverse=True))
    print(similars)

    for element in similars:
        if element[1] >= 0.75 and element[1] != 1:
            print('dodano dopasowane slowo', element)
            user_response_split.append(element[0])


    #support_list.clear()

similar_word_matcher(carBrands)

print(user_response_split)
'''

def test(x):
    print('pocz', x)
    x.append('test')
    #return x

test(brand)

print(brand)