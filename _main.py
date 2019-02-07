from responses import *
from wording import *
import re
from datetime import datetime

user_car_category = []
user_car_brand = []
user_confirmation_response_list = []
user_negation_response_list = []
show_confirmation = []

def hello():
    print(start)


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return ', '.join((a_set & b_set));
    else:
        pass;


def check_response():

    if len(user_negation_response_list) != 0:
        print(loopRestart)
        user_negation_response_list.pop(0)

    user_response = input()
    user_response = re.sub('[.?!@#$]', '', user_response) #kasuje wszystkie znaki specjalne z inputu użytkownika
    user_response_split = user_response.lower().split()

    if any(i in user_response_split for i in carBrands) or any(i in user_response_split for i in carCategories):

        #warunki przy dostarczaniu warunków wyszukiwania pojedyńczo przy wstępnie pustych listach
        if not user_car_category and not user_car_brand:

            #dodanie marki jeśli użytkownik nie sprecyzował wcześniej żadnego parametru
            if any(i in user_response_split for i in carBrands) and not any(i in user_response_split for i in carCategories):
                print('punkt testowy 1')
                user_car_brand.append((common_member(user_response_split, carBrands)).capitalize()) #dodaje marke
                print(selectedBrand.format(user_car_brand[0]))

            #dodanie typu auta jeśli użytkownik nie sprecyzował wcześniej żadnego parametru
            elif any(i in user_response_split for i in carCategories) and not any(i in user_response_split for i in carBrands):
                print('punkt testowy 2')
                user_car_category.append(common_member(user_response_split, carCategories)) #dodaje kategorie
                print(selectedCategory.format(user_car_category[0]))

            #dodanie typu auta oraz marki jeśli użytkownik nie sprecyzował wcześniej żadnego parametru
            elif any(i in user_response_split for i in (carBrands and carCategories)):
                print('punkt testowy 3')
                user_car_brand.append((common_member(user_response_split, carBrands)).capitalize())
                user_car_category.append(common_member(user_response_split, carCategories))
                print('dodano', user_car_brand, user_car_category)

            else:
                pass

        # warunki przy dostarczaniu warunków wyszukiwania pojedyńczo przy wcześniej uzupełnionym 1 parametrze
        elif (len(user_car_brand) > 0) and not user_car_category:

            #dodanie typu auta jeśli użytkownik wcześniej wybrał markę
            if any(i in user_response_split for i in carCategories) and not any(i in user_response_split for i in carBrands):
                print('punkt testowy 4')
                user_car_category.append(common_member(user_response_split, carCategories))
                print('dodano', user_car_category)

        elif (len(user_car_category) > 0) and not user_car_brand:
            #dodanie marki jeśli użytkownik wcześniej wybrał typ auta
            if any(i in user_response_split for i in carBrands) and not any(i in user_response_split for i in carCategories):
                print('punkt testowy 5')
                user_car_brand.append((common_member(user_response_split, carBrands)).capitalize())
                print('dodano', user_car_brand)

        else:
            pass

    elif any(i in user_response_split for i in which) and any(i in user_response_split for i in brand):

        print(list_of_car_manufacturers+(''.join(str(p.capitalize()+'; ') for p in carBrands)))

    elif any(i in user_response_split for i in which) and any(i in user_response_split for i in types):

        print(list_of_car_types+(''.join(str(p+'; ') for p in car_categories_for_listing)))

    elif any(i in user_response_split for i in which) and any(i in user_response_split for i in hour):

        now = datetime.now()
        print(time_now.format(now.hour, now.minute))

    else:
        print(cantFindResponse, 'prz pods')


def check_confirmation():

    #TO SAMO W ZESTAWIE WYZEJ BY ROZPOCZAC KOLEJNY TEMAT PO ZMIANACH
    if len(show_confirmation) == 0:

        print(summaryBothOptions.format(user_car_category[0], user_car_brand[0]))

    show_confirmation.append('showed')

    user_response = input()
    user_response = re.sub('[.?!@#$]', '', user_response)
    user_response_split = user_response.lower().split()


    if any(i in user_response_split for i in confirmation):
        user_confirmation_response_list.append(common_member(user_response, confirmation))

    elif any(i in user_response_split for i in negation):
        print(wrongSummaryMessage)
        user_negation_response_list.append(common_member(user_response, negation))

    else:
        print(cantFindResponseConfirmation.format(user_car_brand, user_car_category), 'przy conf')


def remove_atribute():

    user_response = input()
    user_response = re.sub('[.?!@#$]', '', user_response)
    user_response_split = user_response.lower().split()

    #kasowanie marki auta
    if any(i in user_response_split for i in carBrands) or any(i in user_response_split for i in brand):
        user_car_brand.pop(0)
        show_confirmation.pop(0)
        print(removedSelection)

    # kasowanie wyboru typu auta
    elif any(i in user_response_split for i in carCategories) or any(i in user_response_split for i in types):
        user_car_category.pop(0)
        show_confirmation.pop(0)
        print(removedSelection)

    # kasowanie wyboru marki i typu auta
    elif (any(i in user_response_split for i in carCategories and carBrands)) or any(i in user_response_split for i in everything):
        user_car_category.pop(0)
        user_car_brand.pop(0)
        show_confirmation.pop(0)
        print(removedSelections)

    else:
        print(cantFindResponseConfirmation.format(user_car_brand, user_car_category), 'przy zmianie')

    if any(i in user_response_split for i in confirmation):
        user_confirmation_response_list.append(common_member(user_response, confirmation))

    elif any(i in user_response_split for i in negation):
        print(whatNeedsToBeChanged.format(user_car_brand, user_car_category), 'przy zmianie2')


######################################################################################################################


hello()

while len(user_confirmation_response_list) == 0:

    if len(user_car_brand) == 0 or len(user_car_category) == 0:

        check_response()

    elif len(user_car_brand) != 0 and len(user_car_category) !=0:

        if len(user_negation_response_list) == 0:

            check_confirmation()

        else:

            remove_atribute()


print('Koniec programu. Otrzymano zmienne:', user_car_category, 'oraz', user_car_brand)
