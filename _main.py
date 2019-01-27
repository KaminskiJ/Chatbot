from responses import *
from wording import *
import re


userResponse = ""
userCarCategory = []
userCarBrand = []

userConfirmationResponseList = []
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

def removeUserInput():
    print(wrongSummaryMessage)
    userResponse2 = input()
    userResponse2 = re.sub('[.?!@#$]', '', userResponse2)
    userResponseSplit2 = userResponse2.lower().split()
    #kasowanie wyboru marki
    if any(i in userResponseSplit2 for i in carBrands) or any(i in userResponseSplit2 for i in brand):
        userCarBrand.pop(0)
        print(removedSelection)

    #kasowanie wyboru typu auta
    elif any(i in userResponseSplit2 for i in carCategories) or any(i in userResponseSplit2 for i in types):
        userCarCategory.pop(0)
        print(removedSelection)

    #kasowanie wyboru marki i typu auta
    elif (any(i in userResponseSplit2 for i in carCategories and carBrands)) or any(i in userResponseSplit2 for i in everything):
        userCarCategory.pop(0)
        userCarBrand.pop(0)
        print(removedSelections)

    else:
        print('Nie rozumiem, jednak wszystko jest ok?')
        #dodaj tu potwierdzenie czy moze jednak gra i jesli nie petle od gory tego if'a



def userConfirmationQuestion():
    print(summaryBothOptions.format(userCarCategory[0], userCarBrand[0]))
    userConfirmationResponse = input()
    userConfirmationResponse = userConfirmationResponse.lower().split()

    if any(i in userConfirmationResponse for i in confirmation):
        userConfirmationResponseList.append(commonMember(userConfirmationResponse, confirmation))
    elif any(i in userConfirmationResponse for i in negation):
        removeUserInput()
    #dorzuc tutaj co jak nie rozumie



#na razie wariant dla 1 typu i 1 marki
def checkResponse():

    #na start sprawdzenie czy użytkownik pisze coś na temat samochodów
    if any(i in userResponseSplit for i in carBrands) or any(i in userResponseSplit for i in carCategories):

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
            elif any(i in userResponseSplit for i in (carBrands and carCategories)):
                print('punkt testowy 3')
                addOnlyUserCategory()
                addOnlyUserBrand()
                #print(summaryBothOptions.format(userCarCategory[0], userCarBrand[0]))
                userConfirmationQuestion()

            else:
                pass

        # warunki przy dostarczaniu warunków wyszukiwania pojedyńczo przy wcześniej uzupełnionym 1 parametrze
        elif (len(userCarBrand) > 0) and not userCarCategory:

            #dodanie typu auta jeśli użytkownik wcześniej wybrał markę
            if any(i in userResponseSplit for i in carCategories) and not any(i in userResponseSplit for i in carBrands):
                print('punkt testowy 4')
                addOnlyUserCategory()
                userConfirmationQuestion()

        elif (len(userCarCategory) > 0) and not userCarBrand:

            #dodanie marki jeśli użytkownik wcześniej wybrał typ auta
            if any(i in userResponseSplit for i in carBrands) and not any(i in userResponseSplit for i in carCategories):
                print('punkt testowy 5')
                addOnlyUserBrand()
                userConfirmationQuestion()

    else:
        print(cantFindMatch)

    return userCarBrand, userCarCategory

#Właściwy program wdrażający w życie wszystkie funkcje
hello()

while (len(userCarCategory) == 0) or (len(userCarBrand) == 0) or (userConfirmation != True):

#link ponizej do wdrozenia później - wyszukujący podobieństwa stringów w celu załatwienia końcówe
#https://stackoverflow.com/questions/6690739/fuzzy-string-comparison-in-python-confused-with-which-library-to-use
    userResponse = input()
    userResponse = re.sub('[.?!@#$]', '', userResponse) #kasuje wszystkie znaki specjalne z inputu użytkownika
    userResponseSplit = userResponse.lower().split()

    checkResponse()

    if len(userConfirmationResponseList) != 0:
        userConfirmation = True

print('Koniec programu. Otrzymano zmienne:', userCarCategory, 'i', userCarBrand, '\nW pełnej wersji tego bota zintegrowanym z bazą SQL program '
      'wysłałby poniższą kwerende jako zapytanie dla bazy danych i zwróciłby listę poszukiwanych modeli:')

print('SELECT CarCategoryColumn, CarBrandColumn FROM car_list_table WHERE CarCategoryColumn = {} AND CarBrandColumn = {};'.format(userCarCategory[0], userCarBrand[0]))

