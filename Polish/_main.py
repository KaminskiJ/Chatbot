from functions import *

# global variables used to store final user picks
user_car_category = []
user_car_brand = []
user_confirmation_response_list = []
user_negation_response_list = []
show_summary = []


hello()

while len(user_confirmation_response_list) == 0:

    if len(user_car_brand) == 0 or len(user_car_category) == 0:

        user_input = input()
        corrected_user_input = input_corrector(user_input)

        check_response(corrected_user_input, user_car_category, user_car_brand, user_negation_response_list)

    elif len(user_car_brand) != 0 and len(user_car_category) != 0:

        if len(show_summary) == 0:
            print(summary_both_options.format(user_car_category[0], user_car_brand[0]))
            show_summary.append('showed')

        user_input = input()
        corrected_user_input = input_corrector(user_input)

        if len(user_negation_response_list) == 0:

            check_confirmation(corrected_user_input, user_car_category, user_car_brand, user_confirmation_response_list, user_negation_response_list)

        else:

            remove_atribute(corrected_user_input, user_car_category, user_car_brand, user_confirmation_response_list, user_negation_response_list)


end(user_car_brand, user_car_category)
