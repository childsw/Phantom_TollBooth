from phantom_tollbooth import get_text

remove_list = ['a','an','the',"about", "above", "across", "after", "against", "among", "at", "before", 
                    "behind", "below", "beneath", "beside", "between", "beyond", "by", "despite", "down", "during", 
                    "except", "for", "from", "in", "inside", "into", "near", "of", "off", "on", "over", "past", "since", 
                    "through", "to", "toward", "under", "until", "up", "with", "within", "without","and", "or", "but", 
                    "nor", "for", "yet", "so", "after", "although", "as", "because", "before", 
                    "even if", "even though", "if", "if only", "in order that", "once", "provided that", "rather than", 
                    "since", "so that", "than", "that", "though", "unless", "until", "when", "whenever", "where", "whereas", 
                    "wherever", "whether", "while","i", "me", "we", "us", "you", "he", "him", "she", "her", "it", "they", "them","mine", "ours", "yours", "his", 
                    "hers", "its", "theirs","myself", "yourself", "himself", "herself", "itself", "ourselves", "yourselves", "themselves",
                    "this", "that", "these", "those", "who", "whom", "whose", "which", "what","who", "whom", "whose", "which", "that",
                    "anyone", "anything", "each", "either", "everybody", "neither","nobody", "no one", 
                    "somebody", "someone", "something","all","and,","are","back","be","been","can","could","do","don't","even","had","have","how","i'm",
                    "is","just","im","know","like","little","long","again","get","here","many","more","much","must","my","never","no",
                    "not","now","one","only","other","out","right","said","see","that's","their","then","there","too","very","was","way","well","were",
                    "why","would","your","always","another","any","come","day","didn't","ever","great","look","most","place","same","say","take","thing",
                    "will","can't","did","first","go","last","made","some","soon","use","you'll","away","came",
                    "every","far","few","make","oh","really","side","slowly","sounds","still","went","carefully","exactly",
                    "he'd","heard","ill","new","seemed","seen","youre","yes","were","suddenly","enough",
                    "full","left","several","they're","agreed","set","started","there's","times",
                    "explained","hardly","important","our","perhaps","added","answered","both","does","doesnt","done",
                    "else","end","finally","happened","ive","isnt","knew","let","might","ones","own","dont","thats","everything",
                    "everyone","continued","quite","around","didnt","cant","youll","asked","things","thought","think","replied","looked","along",
                    "going","almost","began","sure","hed","theyre","reached","find","theres","mean"]

def clean_string(book):
    to_replace = [',',';','\"','?','!','\'','.','@','`','(',')','\n',':']
    for i in range(10):# all integers 0-9
        to_replace.append(str(i))# removes integers 0-9
    for i in range (len(to_replace)):# all unwanted characteristics
        book = book.replace(to_replace[i],'')# replaces all characters on to replace list with a space
    return book.lower() #makes all characters lowecase
    '''
    takes string and removes unwanted characters as string

    parameter:
    book(string): the text of phantom tollbooth
    
    returns:
    string: text of phantom tollbooth without unwanted terms and lowercased
    '''


def create_list(book):
    book = book.split()
    return book
    '''
    takes string and forms a list from strings separted by spaces

    parameter:
    cleaned_book(string): the fully cleaned string of the text

    returns:
    list: a list of each word of the phantom tollbooth
    '''

def remove_word(book_list,remove_list):
  
    filtered_list = []
    for word in book_list:
        if word not in remove_list:
            filtered_list.append(word)
    return filtered_list
    '''
    takes list and adds words to an empty list if they are not in the remove list
    
    parameter:
    cleaned_list: the cleaned list of every word
    remove_list: the words to be removed from the cleaned_list
    
    returns:
    list of words that meet the criteria
    '''

def word_count(book_list):
    book_dict = {}
    for word in book_list:
        if word in book_dict:
            book_dict[word] += 1
        else:
            book_dict[word] = 1 # sets initial count of each word to = 1
    return book_dict
    '''
    takes a list of approved words and counts iterations 

    parameter:
    cleaned_list: list with chosen words removed

    returns: 
    dictionary with approved words and relative frequencies
    '''

def print_dict(book_dict):
    book_dict = sorted(book_dict.items(), key=lambda item: item[1], reverse=True)[:50]
    #creates a list of key-value tuple pairs, selects the value item and sorts them. Then selects the first 50 items. 
    print("These are the 50 most popular unique words of the inputted text, the phantom tollbooth")
    for key, value, in book_dict:
        print(f"{key}: {value}") #prints the keys and values with their frequencies 
    '''
    takes the dictionary of words and frequencies and sorts them by frequency then prints them
    as a cleaned print statement showing the keys and values
    
    parameter: 
    dictionary with approved words and their frequencies
    
    returns:
    print statement of words and frequencies
    '''


def main():

    book = get_text()

    cleaned_book = clean_string(book)

    #print(cleaned_book[:1000]) testing: prints the first 1000 characters of string

    cleaned_list = create_list(cleaned_book)

    #print(cleaned_list[:100]) testing: prints the first 100 list items

    cleaned_list = remove_word(cleaned_list,remove_list)

    #print(cleaned_list[:100]) testing: prints the first 100 list items

    cleaned_dict = word_count(cleaned_list)

    #print(cleaned_dict) testing: prints the entire dictionary

    print_dict(cleaned_dict)


if __name__ == '__main__':
    main()