
def read_raw(file):
    '''str->list of str
    Returns a list of strings that was stored in a file.'''
    raw = open(file).read().splitlines()
    for i in range(len(raw)):
        raw[i]=raw[i].strip()
    return raw


def clean_up(l): #currently does not sort in alpha order.
    '''list of str->list of str

    The functions takes as input a list of characters.
    It returns a new list containing the same characters as l except that
    one of each characters that appears odd number of times in l is removed
    and all the * characters are removed

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''


    clean_board=[] 
    for i in l:
        count = 0
        if i != "*":
            if clean_board.count(i) == 0: #checks if character has been seen before
                occurence = l.count(i)
                if occurence%2 == 0: #even occurences adds to board
                    for j in range(occurence):
                        clean_board.append(i)
                elif occurence%2 == 1: # odd case
                    for k in range(occurence-1):
                        clean_board.append(i)                
    
    return clean_board
    


def is_rigorous(l):
    '''list of str->bool
    Returns True if every character in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: You may assume that every element in the list appears even number of times
    (i.e. that the list is clean-up by clean_up function)

    >>> is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    >>> is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''
    list1 = clean_up(l)
    rigorous = True
    i = 0
    while rigorous and i<len(list1):
        if list1.count(list1[i]) != 2:
            rigorous = False
        i+=1
    return rigorous

    
#main
file=input("Enter the name of the file: ")
file=file.strip()
b=read_raw(file)
print("\nBefore clean-up:\n", b)
b=clean_up(b)
print("\nAfter clean-up:\n", b)
if is_rigorous(b):
    print("\nThis list is now rigorous; it has no * and it has "+str(len(b))+" characters.")
else:
    print("\nThis list has no * but is not rigorous and it has "+str(len(b))+" characters.")
     
