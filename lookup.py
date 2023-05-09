import json
import difflib

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

def look_up(word):
    
    if word in data:
        return '\n'.join(data[word])
    matches = difflib.get_close_matches(word, data.keys())
    if matches:
        return '\n'.join(data[matches[0]])        
    else:
        return "Word doesn´t exist, try a different one"



word = input("Tell me the word that you want to Lookup: ").lower()
print(look_up(word))
