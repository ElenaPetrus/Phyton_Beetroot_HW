
from pprint import pprint

# import settings
# from settings import split_into_sentences, count_sentances, count_words_in_text, test_text
from settings import test, test_text
import models.user

import sys

# pprint(split_into_sentences(test_text))
# print('This text contains ', count_sentances(test_text), 'sentences.')
# print('This text contains ', count_words_in_text(test_text), ' words.')
print(test(test_text))
print('User name:', models.user.user_name)


'''The “sys.path” list is initialized from the PYTHONPATH environment variable.

Is it possible to change it from within Python? 
 In order to import modules or packages, they need to reside in one of the paths listed in sys.path. 
 You can modify the sys.path list manually if needed from within Python. 
 It is just a regular list so it can be modified in all the normal ways. 
 For example, you can append to the end of the list using sys.path.append() or to insert in an arbitrary position using sys.path.insert().

If so, does it affect where Python looks for module files? 
Foe ex.  append() is a built-in function of sys module that can be used with path variable to add a specific path for interpreter to search. 
Run some interactive tests to find it out.'''
print(sys.path)
sys.path.append('C:/Users/Desktop')
print('sys.path with APPEND:', sys.path)
