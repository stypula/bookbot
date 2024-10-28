
def main():
    text = getText()
    wordCount = countWords(text)
    mydict = countCharacters(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordCount} words found in the document\n")

    sorted_by_count = sorted( mydict.items(), key=lambda x:x[1], reverse=True)

    sortedDict = dict(sorted_by_count)

    for i in sortedDict:
        print(f"The '{i}' character was found {mydict[i]} times ")

    



    print("--- End report ---")



def getText():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def countWords(text):
    words = text.split()
    count = 0
    for word in words:
        count +=1
    
    return count


def countCharacters(text):
    letter_dict = {}

    for l in text:
        if l.isalpha():
            if l.lower() in letter_dict:
                letter_dict[l.lower()] += 1
            else:
             letter_dict[l.lower()] = 1

    
    return letter_dict



main()