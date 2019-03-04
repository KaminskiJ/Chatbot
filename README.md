# Chatbot

This is my project based on creating interactive rule based chatbot created in python. 
This bot in this demo is trying to support the user with selection of Japanese car. 
In order to so bot asks questions related to car brand as well as car type. When these
two variables are provided and confirmed by the user demo ends. In future versions these
variables will be sent to database where specific car type will be found and presented to
user.

You can find 2 language versions of the same Chatbot in folders included to this 
repository.

note: python 3.3 is necessary for this bot to work.

### Implemented funcitonalities:

Currently bot is able to:
* Collect the user input and modify it. String is collected, all letters are lowered,
special signs are removed.

* Corrected user input is then compared to wording library in order to correct spelling
mistakes. This is done by using default python library called 'difflib' which looks for
similarity ratio between user input and wording list. While certain threshold is met
word is being corrected and added to user input.

* Corrected user input is then checked again against specific wording dictionaries in
order to specify context of user input. Bot then reply according to such input based on
current conversation subject.

### Functionalities to be implemented:

* More context related answers to generic user input.

* Implementation of further discussion after values are selected and user receives 
proposal of specific cars.

* Implementation of multiple answers so that bot does'nt repeats their answers during 
the same conversation cycle (for example when some user selected variables are changed
and conversation loop is starting from the beginning.

* Implementation of more discussion subject not related to main function in order to
make this bot more reliable discussion partner :)

* Code optimization.