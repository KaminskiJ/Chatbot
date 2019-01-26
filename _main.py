from responses import *
from wording import *


userResponse = ""
userCarCategory = []
userCarBrand = []
userConfirmation = False


def hello():
    print(start)

def commonMember(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return ', '.join((a_set & b_set));
    else:
        pass;

def addOnlyUserBrand():
    userCarBrand.append((commonMember(userResponseSplit, carBrands)).capitalize())

def addOnlyUserCategory():
    userCarCategory.append(commonMember(userResponseSplit, carCategories))

#na razie wariant dla 1 typu i 1 marki
def checkResponse():

    #warunki przy dostarczaniu warunków wyszukiwania pojedyńczo przy wstępnie pustych listach
    if not userCarCategory and not userCarBrand:

        #dodanie marki jeśli użytkownik nie sprecyzował wcześniej żadnego parametru
        if any(i in userResponseSplit for i in carBrands) and not any(i in userResponseSplit for i in carCategories):
            print('punkt testowy 1')
            addOnlyUserBrand()
            print(selectedBrand.format(userCarBrand[0]))

        #dodanie typu auta jeśli użytkownik nie sprecyzował wcześniej żadnego parametru
        elif any(i in userResponseSplit for i in carCategories) and not any(i in userResponseSplit for i in carBrands):
            print('punkt testowy 2')
            addOnlyUserCategory()
            print(selectedCategory.format(userCarCategory[0]))

        #dodanie typu auta oraz marki jeśli użytkownik nie sprecyzował wcześniej żadnego parametru
        elif any(i in userResponseSplit for i in carBrands) and any(i in userResponseSplit for i in carCategories):
            print('punkt testowy 3')
            addOnlyUserCategory()
            addOnlyUserBrand()
            print(summaryBothOptions.format(userCarCategory[0], userCarBrand[0]))

    # warunki przy dostarczaniu warunków wyszukiwania pojedyńczo przy wcześniej uzupełnionym 1 parametrze
    elif (len(userCarBrand) > 0) and not userCarCategory:

        #dodanie typu auta jeśli użytkownik wcześniej wybrał markę
        if any(i in userResponseSplit for i in carCategories) and not any(i in userResponseSplit for i in carBrands):
            print('punkt testowy 4')
            addOnlyUserCategory()
            print(summaryBothOptions.format(userCarCategory[0], userCarBrand[0]))

    elif (len(userCarCategory) > 0) and not userCarBrand:

        #dodanie marki jeśli użytkownik wcześniej wybrał typ auta
        if any(i in userResponseSplit for i in carBrands) and not any(i in userResponseSplit for i in carCategories):
            print('punkt testowy 5')
            addOnlyUserBrand()
            print(summaryBothOptions.format(userCarCategory[0], userCarBrand[0]))

    return userCarBrand, userCarCategory

hello()

while (len(userCarCategory) == 0) or (len(userCarBrand) == 0) and not userConfirmation:

    userResponse = input()
    userResponseSplit = userResponse.lower().split()

    checkResponse()

print(userCarCategory, userCarBrand)