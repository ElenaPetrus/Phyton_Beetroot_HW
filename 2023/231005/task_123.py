# Task 1
user_sentance = input('Please write the sentance:')
if len(user_sentance) < 2:
    print('Please write the sentance, that have two letters at least')
else:
    print(user_sentance[:2]+user_sentance[-2:])
