# List of bot responses to user input

start = 'Hello! My name is Eric and I\'m a chatbot created to help you to buy a Japanese car. In order to start I need \nyour decision on what car' \
'manufacturer or car type you take into consideration. Please tell me what would that be?\nIn case you don\'t know what are ' \
'the possible options just ask :-)'


selected_brand = '{} is a very solid car manufacturer! What type of car are you looking for?'

selected_category = 'Alright. So you are interested in {}. What car manufacturer would you like to see?'

summary_both_options = 'Just to be sure allow me to confirm. Would you like to see {} manufactured by {}?'

cant_find_response = 'I\'m really sorry but I don\'t understand :-( Please try to rephrase your response.'

cant_find_response_one_var = 'I\'m really sorry but I don\'t understand :-( Please try to rephrase your response. \nSo far i know that you are interested in {} but I\'m missing information on {}'

car_type = 'what car type you want'

car_brand = 'which car brand you want'

cant_find_response_confirmation = 'I\'m really sorry but I don\'t understand :-( Is selected manufacturer ({}) and car type ({}) correct?'

what_needs_to_be_changed = 'In this care what would you like to change? Selected manufacturer ({}) or car type ({})?'

wrong_summary_message = 'I\'m sorry I must\'ve made a mistake. Please allow me to correct myself! What\'s wrong? Manufacturer or car type?'

removed_selection = 'Ok! I removed this selection. To what would you like to change it?'

removed_selections = 'Ok! My apologies I must\'ve made a mistake.. Please let\'s start from the beginning! :-) What car manufacturer and manufacturer you take into consideration?'

time_now = 'It\'s {}:{}'

list_of_car_manufacturers = 'Here\'s the list of all Japanese car manufacturers: '

list_of_car_types = 'Here\'s the list of all available car types: '

status_missing_brand = 'So far I know that you are interested in {} but I still need you to let me know what car manufacturer would you like o see?'

status_missing_type = 'So far I know that you are interested in {} but I still need you to let me know what car type would you like o see?'

status_missing_both = 'I still don\'t know what are you interested in. Please tell me what car manufacturer and car type you are interested in?'

who_made_you = 'I was made by Jakub Kaminski at the beginning of 2019'

demo_finish = 'End of the demo. Received variables: {} oraz {}.\nThey will be used in below SQL query:\n'

sql_query = '\"SELECT CarCategoryColumn, CarBrandColumn FROM car_list_table WHERE CarCategoryColumn = {} AND CarBrandColumn = {};\"\n'

ending = 'This query is then sent to connected database where it pulls out list of objects that fits selected variables picked by user.' \
         '\nAfter this list is shown further conversation would took place in order to make/change this criteria or to look for specific car offer.'
