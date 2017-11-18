import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    """Return list of found definitions or prints message if not found."""
    if word in data.keys():
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys(), n=1, cutoff=0.8)) > 0:
        close = get_close_matches(word, data.keys(), n=1, cutoff=0.8)[0]
        meant = input("Did you mean '" + close + "'? Yes/No: ").upper()
        if meant == 'Y' or meant == 'YES':
            return translate(close)
        else:
            return "Sorry this word does not exists\n"
    else:
        return "Sorry this word does not exists\n"

word = input('Enter a word: ').lower()

output = translate(word)

if type(output) == list:
    i = 1
    for definition in output:
        print(str(i) + ". " + definition)
    print("")
else:
    print(output)
