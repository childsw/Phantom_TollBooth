import phantom_tollbooth

def main():
    book = phantom_tollbooth.get_text()

    book = book.replace(',',' ')# replaces commas periods and semicolons with spaces to fix the problem ('milo' neq 'milo.' neq 'milo,')
    book = book.replace('.',' ')
    book = book.replace(';',' ')
    book = book.replace('"'," ")
    book = book.replace('?'," ")
    book = book.replace("!"," ")


    book_list = book.lower()#makes all characters lowercase
    book_list = book_list.split()#makes book a list



    articles = ['a','an','the']
    prepositions = ["about", "above", "across", "after", "against", "among", "at", "before", 
                    "behind", "below", "beneath", "beside", "between", "beyond", "by", "despite", "down", "during", 
                    "except", "for", "from", "in", "inside", "into", "near", "of", "off", "on", "over", "past", "since", 
                    "through", "to", "toward", "under", "until", "up", "with", "within", "without",]
    #list of prepositional terms from copilot to save time
    conjunctions = [ "and", "or", "but", "nor", "for", "yet", "so", "after", "although", "as", "because", "before", 
                    "even if", "even though", "if", "if only", "in order that", "once", "provided that", "rather than", 
                    "since", "so that", "than", "that", "though", "unless", "until", "when", "whenever", "where", "whereas", 
                    "wherever", "whether", "while"]
    #list of conjunctions from copilot to save time
    pronouns = ["i", "me", "we", "us", "you", "he", "him", "she", "her", "it", "they", "them","mine", "ours", "yours", "his", 
                "hers", "its", "theirs","myself", "yourself", "himself", "herself", "itself", "ourselves", "yourselves", "themselves",
                "this", "that", "these", "those", "who", "whom", "whose", "which", "what","who", "whom", "whose", "which", "that",
                "anyone", "anything", "each", "either", "everybody", "neither","nobody", "no one", 
                "somebody", "someone", "something"]
    #list of pronouns from copilot to save time
    extra = ["\"and","\"but","\"i","\"you","all","and,","are","back","be","been","can","could","do","don't","even","had","have","how","i'm",
             "is","it\'s","just","im","know","like","little","long","again","get","good","here","many","more","much","must","my","never","no",
             "not","now","one","only","other","out","right","said","see","that's","their","then","there","too","very","was","way","well","were",
             "why","would","your","always","another","any","come","day","didn't","ever","great","look","most","place","same","say","take","thing",
             "three","two","will","alec","can't","did","first","go","last","looking","made","old","some","soon","time","use","you'll","away","came",
             "car","every","far","feet","few","make","oh","really","side","slowly","sounds","still","went","carefully","difficult","door","exactly",
             "he'd","heard","hour","i'll","new","seemed","seen","you're","yes","we're","suddenly","azaz","dodecahedron","dog","dynne","enough","find",
             "full","grew","left","rhyme","several","they're","agreed","bee","demons","face","mean","night","set","started","there's","times","world",
             "years","city","explained","ground","hardly","important","our","perhaps","added","answered","both","boy","does","doesn't","done",
             "eat","else","end","enormous","finally","happened","hard","i've","isn't","knew","let","market","might","milo's","minutes","ones","own",
             "room","should","stood","strange","tell","try","you'd","you've","became","happily","soundkeeper","wagon","afraid","ahead","am","arms",
             "beautiful","better","called","closer","count","dictionopolis","front","giant","half","home","house","it?","'","also","bad","four",
             "good-by","has","kingdom","may","mountains","name","next","name","noise","often","possible","remarked","royal","sadly","sat","short",
             "softly","took","trees","valley","want","we'll","whole","wrong","book","please","answer","being","bit","color","busy","completely","different",
             "dischord","distance","doctor","doing","earl","family","finished","floor","followed","forest","gasped","gone","hand","happy","high","immediately",
             "keep","land","mouth","put","question","rest","roared","silence","spoke","such","suggested","terribly","they'd","tried","true","used","walked","wasn't",
             "watchdog","word","princesses","standing","leaped"]
    #more words to remove because they are not on the tag crowd 50 words

    filtered_words = []

    for word in book_list:#removes strings in lists from book_list and then appends them to a list
        if word not in conjunctions and word not in prepositions and word not in articles and word not in pronouns and word not in extra:
            filtered_words.append(word)

    # sort the remaining words a-z
    sorted_words = sorted(filtered_words)

    # adds count for each word +1
    word_count = {}
    for word in sorted_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_word_dict = {key: value for key, value in sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:50]}
    #sorts words by their values from highest to lowest
    #I had piece of this idea but needed copilots help to get the finishing pieces, particularly the sorted section with lamda function, reverse statement
    #the [:50] selects the highest 50 items
    
    sorted_50_words = {key: sorted_word_dict[key] for key in sorted(sorted_word_dict.keys())}
    #sorts keys a-z

    for keys, values in sorted_50_words.items():
        print(f"{keys}:{values}") 


if __name__ == '__main__':
    main()