from functions import *

# global variables used to store final user picks and trigger contextual dialogue options
user_car_category = []  # user selected car category
user_car_brand = []  # user selected car brand
user_confirmation_response_list = []  # variable used to confirm user selection and termination of program
user_negation_response_list = []  # variable used to trigger loop used for data correction
show_summary = []  # variable used to print selection summary just once and not during each iteration of bot loop
correction_context = []  # variable used to define context of user response during correction of user selection


hello()

# initial bot loop working until user selects two search attributes and confirm them
while len(user_confirmation_response_list) == 0:

    # loop working until two attributes are selected
    if len(user_car_brand) == 0 or len(user_car_category) == 0:

        user_input = input()
        corrected_user_input = input_corrector(user_input)

        check_response(corrected_user_input, user_car_category, user_car_brand, user_negation_response_list, correction_context)

    # loop used to confirm or correct selected attributes
    elif len(user_car_brand) != 0 and len(user_car_category) != 0:

        if len(show_summary) == 0:
            print(summary_both_options.format(user_car_category[0], user_car_brand[0]))
            show_summary.append('showed')

        user_input = input()
        corrected_user_input = input_corrector(user_input)

        if len(user_negation_response_list) == 0:

            check_confirmation(corrected_user_input, user_car_category, user_car_brand, user_confirmation_response_list, user_negation_response_list)

        else:

            remove_attribute(corrected_user_input, user_car_category, user_car_brand, user_confirmation_response_list, user_negation_response_list, show_summary, correction_context)

# bot demo end message
end(user_car_brand, user_car_category)
