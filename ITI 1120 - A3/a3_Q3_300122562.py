def longest_run(numbers):
    """[list] -> int
    counts the longest run in a list
    precondition: list only contains numbers and spaces
    """
    longest = 0
    current_length = 0
    for i in range(len(numbers)):
        if i == 0:
            current_length = 1
        elif i!=0 and numbers[i] == numbers[i-1]:
            current_length += 1
        else:
            current_length = 1
        if current_length>longest:
            longest = current_length
    return longest


#input
sequence = (input("Pleast input a list of numbers seperated by spaces: ").strip().split(" "))
sequence_list = []               
for i in range(len(sequence)): #converts to int
    if sequence[i] != "":
        sequence_list.append(float(sequence[i]))
print(longest_run(sequence_list))
