import re
import difflib
from wording import *
from responses import *
from datetime import datetime


def hello():
    print(start)


# function that creates two sets (lists w/o duplicates) and return new list of common words
# this is used to look for key words in user input within included dictionaries
def common_member(first_list, second_list):
    first_list_set = set(first_list)
    second_list_set = set(second_list)
    if first_list_set & second_list_set:
        return ', '.join((first_list_set & second_list_set))
    else:
        pass


# function used to correct used input before comparison with dictionaries
def input_corrector(user_input):
    corrected_input = re.sub('[.?!@#$]', '', user_input)  # removes all special symbols from user input
    corrected_input_split = corrected_input.lower().split()  # splits the corrected input
    weighted_results = []  # support list with weighted result of word similarities
    corrected_words = []   # support list of words corrected by function

    # ---single comparison block start---
    # Here each word in user input is compared to all dictionaries in order to look for similar words. Each word
    # is compared between two lists and ratio of they similarity is detected. Then new list with these data is created
    # Currently it's rather raw format with duplicated code and not iterated by dictionary name as data format
    # would have to be changed. This will be done in future bot version
    working_input = corrected_input_split.copy()

    while len(working_input) > 0:

        for entry in carBrands:  # car brands comparison
            ratio = difflib.SequenceMatcher(None, entry, working_input[0]).ratio()
            weighted_results.append((entry, ratio))

        working_input.pop(0)

    # ---single comparison block end---

    working_input = corrected_input_split.copy()

    while len(working_input) > 0:

        for entry in carCategories:  # car categories comparison
            ratio = difflib.SequenceMatcher(None, entry, working_input[0]).ratio()
            weighted_results.append((entry, ratio))

        working_input.pop(0)

    # Here all compared elements in newly created list are being reviewed based on their similarity.
    # If threshold is met then a word is being appended to corrected list which is then added to user input
    for element in weighted_results:
        if element[1] >= 0.75 and element[1] != 1:  # first condition here is a minimum similarity ratio
            corrected_words.append(element[0])

    corrected_user_input = list(set(corrected_input_split + corrected_words))

    return corrected_user_input


# function used to check user input against dictionaries and respond accordingly
def check_response(corrected_user_input, user_car_category, user_car_brand, user_negation_response_list):

    # first section printed only when whole loop is being started again after data correction is made
    if len(user_negation_response_list) != 0 and len(user_car_category) == 0 and len(user_car_brand) == 0:
        print(removed_selections)
        user_negation_response_list.pop(0)

    # conditions if user input consist either car brand or car type
    if any(i in corrected_user_input for i in carBrands) or any(i in corrected_user_input for i in carCategories):

        # conditions when user provide necessary answers one by one with nothing yet selected
        if not user_car_category and not user_car_brand:

            # car brand addition
            if any(i in corrected_user_input for i in carBrands) and not any(i in corrected_user_input for i in carCategories):
                user_car_brand.append((common_member(corrected_user_input, carBrands)).capitalize())
                print(selected_brand.format(user_car_brand[0]))

            # car type addition
            elif any(i in corrected_user_input for i in carCategories) and not any(i in corrected_user_input for i in carBrands):
                user_car_category.append(common_member(corrected_user_input, carCategories))
                print(selected_category.format(user_car_category[0]))

            # both parameters addition
            elif any(i in corrected_user_input for i in (carBrands and carCategories)):
                user_car_brand.append((common_member(corrected_user_input, carBrands)).capitalize())
                user_car_category.append(common_member(corrected_user_input, carCategories))

            else:
                pass

        # conditions when user provide necessary answers one by one with 1 condition added previously
        elif (len(user_car_brand) > 0) and not user_car_category:

            # addition of car type if user picked car brand previously
            if any(i in corrected_user_input for i in carCategories) and not any(i in corrected_user_input for i in carBrands):
                user_car_category.append(common_member(corrected_user_input, carCategories))

        elif (len(user_car_category) > 0) and not user_car_brand:

            # addition of car brand if user picked car type previously
            if any(i in corrected_user_input for i in carBrands) and not any(i in corrected_user_input for i in carCategories):
                user_car_brand.append((common_member(corrected_user_input, carBrands)).capitalize())

        else:
            pass

    # other various responses not connected with main discussion subject like what car manufacturers are available
    # what data bot is still missing, what is the time etc.
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

    # various responses if bot doesn't understand user input
    elif len(user_car_category) == 0 and len(user_car_brand) != 0:
        print(cant_find_response_one_var.format(user_car_brand[0], car_type))

    elif len(user_car_brand) == 0 and len(user_car_category) != 0:
        print(cant_find_response_one_var.format(user_car_category[0], car_brand))

    else:
        print(cant_find_response)


# function used after both necessary condition are provided in order to confirm or correct them
def check_confirmation(corrected_user_input, user_car_category, user_car_brand, user_confirmation_response_list, user_negation_response_list):

    if any(i in corrected_user_input for i in confirmation):
        user_confirmation_response_list.append('confirmed')

    elif any(i in corrected_user_input for i in negation):
        print(wrong_summary_message)
        user_negation_response_list.append('negated')

    else:
        print(cant_find_response_confirmation.format(user_car_brand[0], user_car_category[0]))


# function used to remove incorrect search condition if user didn't confirm them
def remove_attribute(corrected_user_input, user_car_category, user_car_brand, user_confirmation_response_list, user_negation_response_list, show_summary):

    # removing car brand selection
    if any(i in corrected_user_input for i in carBrands) or any(i in corrected_user_input for i in brand):
        user_car_brand.pop(0)
        user_negation_response_list.pop(0)
        show_summary.pop(0)
        print(removed_selection)

    # removing car type selection
    elif any(i in corrected_user_input for i in carCategories) or any(i in corrected_user_input for i in types):
        user_car_category.pop(0)
        user_negation_response_list.pop(0)
        show_summary.pop(0)
        print(removed_selection)

    # removing of both selections
    elif (any(i in corrected_user_input for i in carCategories and carBrands)) or any(i in corrected_user_input for i in everything):
        user_car_category.pop(0)
        user_car_brand.pop(0)
        user_negation_response_list.pop(0)
        show_summary.pop(0)

    # another chance to confirm that data is correct if this loop was triggered accidentally
    elif any(i in corrected_user_input for i in confirmation):
        user_confirmation_response_list.append('confirmed')

    #
    elif any(i in corrected_user_input for i in negation):
        print(what_needs_to_be_changed.format(user_car_brand[0], user_car_category[0]))

    else:
        print(cant_find_response_confirmation.format(user_car_brand[0], user_car_category[0]))

def end(user_car_brand, user_car_category):
    print(demo_finish.format(user_car_brand[0], user_car_category[0]))
    print(sql_query.format(user_car_brand[0], user_car_category[0]))
    print(ending)
