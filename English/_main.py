from responses import *
from wording import *
import re, difflib
from datetime import datetime

user_car_category = []
user_car_brand = []
user_confirmation_response_list = []
user_negation_response_list = []
show_confirmation = []
support_list = []
weighted_results = []
user_response_split = []
corrected_words = []
user_response_split_corrected = []

def hello():
    print(start)

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return ', '.join((a_set & b_set));
    else:
        pass;

def similar_word_matcher(user_list, wording_list):

    while len(user_list) > 0:

        for result in wording_list:
            ratio = difflib.SequenceMatcher(None, result, user_list[0]).ratio()
            weighted_results.append((result, ratio))

        user_list.pop(0)

    similars = (sorted(weighted_results, key=lambda x: x[1], reverse=True))

    for element in similars:
        if element[1] >= 0.75 and element[1] != 1:
            corrected_words.append(element[0])

def text_corrections(text):

    #this function cannot yet be normally iterated as list are not created as classes - callback to their name\
    #is impossible in current data format. This will be corrected on a later stage

    support_list = text.copy()
    similar_word_matcher(support_list, goodbye)
    support_list = text.copy()
    similar_word_matcher(support_list, carCategories)
    support_list = text.copy()
    similar_word_matcher(support_list, carBrands)
    support_list = text.copy()
    similar_word_matcher(support_list, confirmation)
    support_list = text.copy()
    similar_word_matcher(support_list, negation)
    support_list = text.copy()
    similar_word_matcher(support_list, brand)
    support_list = text.copy()
    similar_word_matcher(support_list, types)
    support_list = text.copy()
    similar_word_matcher(support_list, everything)
    support_list = text.copy()
    similar_word_matcher(support_list, which)
    support_list = text.copy()
    similar_word_matcher(support_list, hour)
    support_list = text.copy()
    similar_word_matcher(support_list, what)
    support_list = text.copy()
    similar_word_matcher(support_list, who)
    support_list = text.copy()
    similar_word_matcher(support_list, made)

    return corrected_words

def check_response():

    if len(user_negation_response_list) != 0 and len(user_car_category) == 0 and len(user_car_brand) == 0:
        print(removed_selections)
        user_negation_response_list.pop(0)

    user_response = input()
    user_response = re.sub('[.?!@#$]', '', user_response) #kasuje wszystkie znaki specjalne z inputu użytkownika
    user_response_split = user_response.lower().split()

    text_corrections(user_response_split)

    user_response_split_corrected = list(set(user_response_split + corrected_words))


    if any(i in user_response_split_corrected for i in carBrands) or any(i in user_response_split_corrected for i in carCategories):

        #conditions when user provide necessary answers one by one with nothing selected
        if not user_car_category and not user_car_brand:

            #car brand addition
            if any(i in user_response_split_corrected for i in carBrands) and not any(i in user_response_split_corrected for i in carCategories):
                #print('punkt testowy 1')
                user_car_brand.append((common_member(user_response_split_corrected, carBrands)).capitalize()) #dodaje marke
                print(selected_brand.format(user_car_brand[0]))

            #car type addition
            elif any(i in user_response_split_corrected for i in carCategories) and not any(i in user_response_split_corrected for i in carBrands):
                #print('punkt testowy 2')
                user_car_category.append(common_member(user_response_split_corrected, carCategories)) #dodaje kategorie
                print(selected_category.format(user_car_category[0]))

            #both parameters addition
            elif any(i in user_response_split_corrected for i in (carBrands and carCategories)):
                #print('punkt testowy 3')
                user_car_brand.append((common_member(user_response_split_corrected, carBrands)).capitalize())
                user_car_category.append(common_member(user_response_split_corrected, carCategories))
                #print('I\'ve added:', user_car_brand[0],'and', user_car_category[0])

            else:
                pass

        #conditions when user provide necessary answers one by one with 1 condition added previously
        elif (len(user_car_brand) > 0) and not user_car_category:
            #addition of car type if user picked car brand previously
            if any(i in user_response_split_corrected for i in carCategories) and not any(i in user_response_split_corrected for i in carBrands):
                #print('punkt testowy 4')
                user_car_category.append(common_member(user_response_split_corrected, carCategories))
                #print('I\'ve added:', user_car_category[0])

        elif (len(user_car_category) > 0) and not user_car_brand:
            #addition of car brand if user picked car type previously
            if any(i in user_response_split_corrected for i in carBrands) and not any(i in user_response_split_corrected for i in carCategories):
                #print('punkt testowy 5')
                user_car_brand.append((common_member(user_response_split_corrected, carBrands)).capitalize())
                #print('I\'ve added:', user_car_brand[0])

        else:
            pass

    elif any(i in user_response_split_corrected for i in which) and any(i in user_response_split_corrected for i in brand):

        print(list_of_car_manufacturers+(''.join(str(p.capitalize()+'; ') for p in carBrands)))

    elif any(i in user_response_split_corrected for i in which) and any(i in user_response_split_corrected for i in types):

        print(list_of_car_types+(''.join(str(p+'; ') for p in car_categories_for_listing)))

    elif any(i in user_response_split_corrected for i in what) and any(i in user_response_split_corrected for i in missing):

        if len(user_car_category) == 0 and len(user_car_brand) > 0:
            print(status_missing_type.format(user_car_brand[0]))

        elif len(user_car_category) > 0 and len(user_car_brand) == 0:
            print(status_missing_brand.format(user_car_category[0]))

        elif len(user_car_category) == 0 and len(user_car_brand) == 0:
            print(status_missing_both)

        else:
            pass

    elif any(i in user_response_split_corrected for i in which) and any(i in user_response_split_corrected for i in hour):

        now = datetime.now()
        print(time_now.format(now.hour, now.minute))

    elif any(i in user_response_split_corrected for i in who) and any(i in user_response_split_corrected for i in made):
        print(who_made_you)

    else:
        print(cant_find_response)

    #prints for testing purposes
    #print('surowa wiad', user_response_split)
    #print('popr wiad', user_response_split_corrected)
    #print('wybrana marka', user_car_brand)
    #print('wybrana kateg', user_car_category)

def check_confirmation():

    if len(show_confirmation) == 0:

        print(summary_both_options.format(user_car_category[0], user_car_brand[0]))

    show_confirmation.append('showed')

    user_response = input()
    user_response = re.sub('[.?!@#$]', '', user_response)
    user_response_split = user_response.lower().split()

    text_corrections(user_response_split)

    user_response_split_corrected = list(set(user_response_split + corrected_words))


    if any(i in user_response_split_corrected for i in confirmation):
        user_confirmation_response_list.append(common_member(user_response, confirmation))

    elif any(i in user_response_split_corrected for i in negation):
        print(wrong_summary_message)
        user_negation_response_list.append(common_member(user_response, negation))

    else:
        print(cant_find_response_confirmation.format(user_car_brand[0], user_car_category[0]))

def remove_atribute():

    user_response = input()
    user_response = re.sub('[.?!@#$]', '', user_response)
    user_response_split = user_response.lower().split()

    text_corrections(user_response_split)

    user_response_split_corrected = list(set(user_response_split + corrected_words))

    #removing car brand selection
    if any(i in user_response_split_corrected for i in carBrands) or any(i in user_response_split_corrected for i in brand):
        user_car_brand.pop(0)
        show_confirmation.pop(0)
        print(removed_selection)

    #removing car type selection
    elif any(i in user_response_split_corrected for i in carCategories) or any(i in user_response_split_corrected for i in types):
        user_car_category.pop(0)
        show_confirmation.pop(0)
        print(removed_selection)

    #removing of both selections
    elif (any(i in user_response_split_corrected for i in carCategories and carBrands)) or any(i in user_response_split_corrected for i in everything):
        user_car_category.pop(0)
        user_car_brand.pop(0)
        show_confirmation.pop(0)

    else:
        print(cant_find_response_confirmation.format(user_car_brand[0], user_car_category[0]))

    if any(i in user_response_split_corrected for i in confirmation):
        user_confirmation_response_list.append(common_member(user_response, confirmation))

    elif any(i in user_response_split_corrected for i in negation):
        print(what_needs_to_be_changed.format(user_car_brand[0], user_car_category[0]))

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


print(demo_finish.format(user_car_brand[0],user_car_category[0]))
print(sql_query.format(user_car_brand[0], user_car_category[0]))
print(ending)
