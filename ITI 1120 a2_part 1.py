def ascii_name_plaque(name):
    """(string) -> string
    takes name inputed and creates a name plaque
    Preconditions: input must be a string"""
    # creating elements for plaque
    space = " "
    star = "*"
    # determining size of frame according to name provided
    length = len(name)
    name_layer = star + space + "__" + name + "__" + space + star
    top_bottom = star * (length + 8)
    whitespace = star + space * (length + 6) + star
    print(top_bottom + "\n" + whitespace + "\n" + name_layer + "\n" + whitespace + "\n" + top_bottom)
    return


def splitter(num, split):
    """ (int,int)->string
     splits given number into numbers of digit length "split"
    precondition: num and split must be positive integers.
    """
    total_digits = len(str(num))  # determining # of digits in num
    new_digits = []  # creating array to store new digits
    if total_digits % split == 0:  # num can be evenly split
        num_splits = total_digits // split
        digs = split
        for i in range(0, num_splits):
            # isolate required leading digits
            digit_power = 10 ** (total_digits - digs)
            digit = num // digit_power
            # add new number to array
            new_digits.append(digit)
            num -= digit * digit_power
            digs += split
        print(new_digits)
        return new_digits
    else:
        print("invalid input ")
    return


def split_tester(num, split):
    """ (str, str) -> str
    determines if numbers of num split into smaller digits are in increasing order
    precondition: num and split must be positive integers
    """
    # converting inputs to strings and striping empty space
    num_string = str(num).strip()
    split_string = str(split).strip()
    # converting to integer to split
    num = int(num_string)
    split = int(split_string)
    # using splitter function to create new digits
    digits = splitter(num, split)
    # whether numbers are in increasing order
    tester = True
    for i in range(len(digits) - 1):
        tester = digits[i + 1] >= digits[i]
        if not tester:
            break
    return tester


def all_nums(s):
    """(str) -> bool
    parses through a string to determine if all characters are numbers
    preconditions: none"""
    for char in s:
        status = char in '1234567890'
        if not status:
            break  # ends loop at with status being false
    return status


def play():
    """() -> string
    requests values to run split tester and tells user outcome in sentence
    preconditions: none """
    print("Great choice!")
    # determining whether number is valid
    n = False
    while not n:
        number = input("Enter a positive integer: ")
        if not all_nums(number):
            print("The input can only be digits ")
        elif float(number) <= 0:
            print("Please enter a number greater than 0")
        elif float(number) % 1 != 0:
            print("input can only contain whole numbers")
        else:
            n = True
    # getting split value and determining if it is valid
    m = False
    while not m:
        splice = input("Input the split, The split has to divide the length of " + str(number) + " i.e: " + str(
            len(str(number))) + ": ")
        if not all_nums(splice):
            print("The input can only be digits ")
            splice = input("Enter a positive integer: ")
        elif float(splice) <= 0:
            print("Please enter a number greater than 0")
            splice = input("Enter a positive integer: ")
        elif float(splice) % 1 != 0:
            print ("input can only contain whole numbers")
            splice = input("Enter a positive integer: ")
        else:
            m = True
    # output
    results = split_tester(number, splice)
    if results:
        print("The sequence is increasing")
    else:
        print("The sequence is not increasing")
    return


def welcome():
    """() -> str
    Welcomes user to split tester
    precondition: none
    """
    ascii_name_plaque("Welcome to my increasing split tester")
    name = input("What is your name? ")
    ascii_name_plaque(name + ", welcome to my increasing split tester")
    # player choosing to play
    player = input(
        name + ", would you like to test if a number admits an increasing split of give size?").strip().lower()
    while player != 'no' and player != 'yes':  # if player input invalid answer
        print("Incorrect input. Please answer yes or no")
        player = input(name + ", would you like to test if a number admits an increasing split of give size?")
    while player == 'yes':  # if player chooses to play
        play()
        player = input(
            name + ", would you like to test if a number admits an increasing split of give size?").strip().lower()
    if player == "no":
        return ascii_name_plaque("Goodbye " + name)


welcome()
