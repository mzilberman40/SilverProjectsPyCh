import re


def clean_phrase(phrase):
    # Removing extra spaces (start, end and more then one between words)
    phrase = ' '.join(phrase.strip().split())
    # Removing all symbols excluding spaces and letters of alphabet
    reg = re.compile('[\w ]+')
    return ''.join(reg.findall(phrase)).lower()



