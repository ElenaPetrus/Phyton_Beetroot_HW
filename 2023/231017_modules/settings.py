import re
from pprint import pprint


test_text = open('chapter1.txt').read()


def split_into_sentences(t):
    pattern = r'(?<=[.!?])\s+(?=[A-Z])|\n{2,}'
    split = re.split(pattern, t)
    result = []
    for part_of_text in split:
        if not part_of_text:
            continue
        elif not re.match(pattern, part_of_text):
            result.append(part_of_text)
        else:
            result[-1] += part_of_text[0]
    return (result)


def count_sentances(t):
    quantity_sentances = len(split_into_sentences(t))
    return quantity_sentances


def count_words_in_text(t):
    sentance_list = split_into_sentences(t)
    quantity_words = 0
    for i in sentance_list:
        word_list = re.findall(r'\b\w+\b', i)
        quantity_words += len(word_list)
    return quantity_words


def test(t):
    print('This text contains ', count_sentances(t), 'sentences.')
    print('This text contains ', count_words_in_text(t), ' words.')


if __name__ == "__main__":
    print("I'm running as a script!")
