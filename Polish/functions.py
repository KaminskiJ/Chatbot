import re
import difflib
from wording import *
from responses import *
from datetime import datetime


def hello():
    print(start)


def common_member(first_list, second_list):
    first_list_set = set(first_list)
    second_list_set = set(second_list)
    if (first_list_set & second_list_set):
        return ', '.join((first_list_set & second_list_set))
    else:
        pass


def input_corrector(user_input):
    corrected_input = re.sub('[.?!@#$]', '', user_input)  # removes all special symbols from user input
    corrected_input_split = corrected_input.lower().split()  # splits the corrected input
    weighted_results = []  # support list with weighted result of word similarities
    corrected_words = []   # support list of words corrected by function

    working_input = corrected_input_split.copy()

    while len(working_input) > 0:

        for entry in carBrands:  # tutaj na bazie z markami aut
            ratio = difflib.SequenceMatcher(None, entry, working_input[0]).ratio()
            weighted_results.append((entry, ratio))

        working_input.pop(0)

    working_input = corrected_input_split.copy()

    while len(working_input) > 0:

        for entry in carCategories:  # tutaj na bazie z typami aut
            ratio = difflib.SequenceMatcher(None, entry, working_input[0]).ratio()
            weighted_results.append((entry, ratio))

        working_input.pop(0)

    for element in weighted_results:
        if element[1] >= 0.75 and element[1] != 1:
            corrected_words.append(element[0])

    corrected_user_input = list(set(corrected_input_split + corrected_words))

    return corrected_user_input


def check_response(corrected_user_input, user_car_category, user_car_brand, user_negation_response_list):

    if len(user_negation_response_list) != 0 and len(user_car_category) == 0 and len(user_car_brand) == 0:
        print(removed_selections)
        user_negation_response_list.pop(0)

    if any(i in corrected_user_input for i in carBrands) or any(i in corrected_user_input for i in carCategories):

        #conditions when user provide necessary answers one by one with nothing selected
        if not user_car_category and not user_car_brand:

            #car brand addition
            if any(i in corrected_user_input for i in carBrands) and not any(i in corrected_user_input for i in carCategories):
                #print('punkt testowy 1')
                user_car_brand.append((common_member(corrected_user_input, carBrands)).capitalize()) #dodaje marke
                print(selected_brand.format(user_car_brand[0]))

            #car type addition
            elif any(i in corrected_user_input for i in carCategories) and not any(i in corrected_user_input for i in carBrands):
                #print('punkt testowy 2')
                user_car_category.append(common_member(corrected_user_input, carCategories)) #dodaje kategorie
                print(selected_category.format(user_car_category[0]))

            #both parameters addition
            elif any(i in corrected_user_input for i in (carBrands and carCategories)):
                #print('punkt testowy 3')
                user_car_brand.append((common_member(corrected_user_input, carBrands)).capitalize())
                user_car_category.append(common_member(corrected_user_input, carCategories))
                #print('dodano', user_car_brand[0], user_car_category[0])

            else:
                pass

        #conditions when user provide necessary answers one by one with 1 condition added previously
        elif (len(user_car_brand) > 0) and not user_car_category:
            #addition of car type if user picked car brand previously
            if any(i in corrected_user_input for i in carCategories) and not any(i in corrected_user_input for i in carBrands):
                #print('punkt testowy 4')
                user_car_category.append(common_member(corrected_user_input, carCategories))
                #print('dodano', user_car_category[0])

        elif (len(user_car_category) > 0) and not user_car_brand:
            #addition of car brand if user picked car type previously
            if any(i in corrected_user_input for i in carBrands) and not any(i in corrected_user_input for i in carCategories):
                #print('punkt testowy 5')
                user_car_brand.append((common_member(corrected_user_input, carBrands)).capitalize())
                #print('dodano', user_car_brand[0])

        else:
            pass

    elif any(i in corrected_user_input for i in which) and any(i in corrected_user_input for i in brand):

        print(list_of_car_manufacturers+(''.join(str(p.capitalize()+'; ') for p in carBrands)))

    elif any(i in corrected_user_input for i in which) and any(i in corrected_user_input for i in types):

        print(list_of_car_types+(''.join(str(p+'; ') for p in car_categories_for_listing)))

    elif any(i in corrected_user_input for i in what) and any(i in corrected_user_input for i in missing):

        if len(user_car_category) == 0 and len(user_car_brand) > 0:
            print(status_missing_type.format(user_car_brand[0]))

        elif len(user_car_category) > 0 and len(user_car_brand) == 0:
            print(status_missing_brand.format(user_car_category[0]))

        elif len(user_car_category) == 0 and len(user_car_brand) == 0:
            print(status_missing_both)

        else:
            pass

    elif any(i in corrected_user_input for i in which) and any(i in corrected_user_input for i in hour):

        now = datetime.now()
        print(time_now.format(now.hour, now.minute))

    elif any(i in corrected_user_input for i in who) and any(i in corrected_user_input for i in made):
        print(who_made_you)

    else:
        print(cant_find_response)


def check_confirmation(corrected_user_input, user_car_category, user_car_brand, user_confirmation_response_list, user_negation_response_list):

    if any(i in corrected_user_input for i in confirmation):
        user_confirmation_response_list.append('confirmed')

    elif any(i in corrected_user_input for i in negation):
        print(wrong_summary_message)
        user_negation_response_list.append('negated')

    else:
        print(cant_find_response_confirmation.format(user_car_brand[0], user_car_category[0]))


def remove_atribute(corrected_user_input, user_car_category, user_car_brand, user_confirmation_response_list, user_negation_response_list):

    # removing car brand selection
    if any(i in corrected_user_input for i in carBrands) or any(i in corrected_user_input for i in brand):
        user_car_brand.pop(0)
        user_negation_response_list.pop(0)
        print(removed_selection)

    # removing car type selection
    elif any(i in corrected_user_input for i in carCategories) or any(i in corrected_user_input for i in types):
        user_car_category.pop(0)
        user_negation_response_list.pop(0)
        print(removed_selection)

    # removing of both selections
    elif (any(i in corrected_user_input for i in carCategories and carBrands)) or any(i in corrected_user_input for i in everything):
        user_car_category.pop(0)
        user_car_brand.pop(0)
        user_negation_response_list.pop(0)

    else:
        print(cant_find_response_confirmation.format(user_car_brand[0], user_car_category[0]))

    if any(i in corrected_user_input for i in confirmation):
        user_confirmation_response_list.append('confirmed')

    elif any(i in corrected_user_input for i in negation):
        print(what_needs_to_be_changed.format(user_car_brand[0], user_car_category[0]))


def end(user_car_brand, user_car_category):
    print(demo_finish.format(user_car_brand[0], user_car_category[0]))
    print(sql_query.format(user_car_brand[0], user_car_category[0]))
    print(ending)
