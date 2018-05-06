import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data=json.load(open("C:/Python36/working_files/data.json"))      #data.json file has been uploaded in read mode
'''print (data)
print("\n")
print(type(data))
print(data["rain"])
'''

def translate(word):
    word=word.lower()

    if(word in data):
        return data[word]

    elif(word.capitalize() in data):
        return data[word.capitalize()]

    elif len(get_close_matches(word, data.keys(), cutoff=0.8))>0:
        print( "Did you mean %s instead? " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        yesorno=input("y or n : ")
        if (yesorno=='y'):
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif(yesorno=='n'):
            return "Sorry, We dont know what you are trying to search for"
        else:
            return "Sorry!, we don't know what you are trying to do"

    else:
        return "Sorry, We dont know what you are trying to search for"


ch='y'
while(ch=='y'):
    word=input("Enter word:")

    output=translate(word)
    if type(output)==list:
        for item in output:
            print (item)
    else :
        print(output)

    ch=input("\nDo you want to search for more words? (y or n) :")

