import string

def open_file():
    '''None->file object
    opens file based on user inputed text'''
    file_name = None
    while file_name == None:
        try:
            file_name=input("Enter the name of the file: ").strip()
            f=open(file_name)
            f.close()
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
            file_name=None
    return open(file_name).read()

def process_lines(lines):
    ''' (list)-> 2d list
    takes list of phrases and removes numbers and punctuation
    preconditions:none
    '''
    sentences = []
    # string pre-processing
    for phrase in lines:
        split_line = phrase.split(" ")
        line = []
        for words in split_line:
            word = ''
            for char in words:
                if char.isalpha():
                    word += char
            if len(word)>1:
                line.append(word)      
        sentences.append(line)
    return sentences

def process_word(word):
    '''(str)->str
    returns given word without punctuation and in lowercase
    '''
    clean_word = ''
    for i in word:
        if i.isalpha() == True:
            clean_word+=i.lower()
    return clean_word

def make_dict(sentences):
    '''(2dlist) -> dict
    make dictionary on word locations in series of sentence
    precondition  : none
    '''
    dictionary = {}
    # dictionary / word counting
    for i in range(len(sentences)):
        for word in sentences[i]:
            if word in dictionary and (i+1) not in dictionary[word]: # searches that word key exists already
                y=dictionary[word]
                y.append(i+1)
            else: # creates new key if necessary
                dictionary[word] = [i+1]
    return dictionary

def read_file(fp): # currently exists error with 1s
    '''(file object)->dict
    See the assignment text for what this function should do'''
    lines = fp.lower().splitlines()
    sentences = process_lines(lines)
    diction = make_dict(sentences)   
    return diction
                
def is_valid(D, query):
    ''' (dict, str) ->bool
    checks that query words/ input are correct keys for dictionary
    '''
    words = query.strip().split()
    for i in words:
        if i not in D:
            return False
        else:
            return True
            

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do
    precondition: none
    '''
    commonalities = []
    if is_valid(D,query) == True:
        words = query.strip().split()
        if len(words) == 1: # finding occurences of single word
            for j in D[query]:
                commonalities.append(j)
        else:
            for i in range(len(words)-1): # key and its sentence numbers
                for j in D[words[i]]:
                    for k in D[words[i+1]]:
                        if j == k and j not in commonalities:
                            commonalities.append(j)
    else:
        return 'Word '+ str(query)+' not in file'
    return commonalities
    
    

##############################
# main
##############################
file=open_file()
d=read_file(file)

query_more = True
while query_more == True:
    query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip()
    if query.lower() == 'q':
        query_more = False
    else:
        print(find_coexistance(d,process_word(query)))
