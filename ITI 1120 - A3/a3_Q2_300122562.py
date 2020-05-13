def two_length_run(numbers):
    """[list of numbers] -> bool
    returns true if list has numbers repeating at least 2 times in a row
    :parameter numbers is a list
    """
    repeat = False
    i = 0
    while i < (len(numbers) - 1) and repeat == False:
        repeat = numbers[i] == numbers[i + 1]
        i += 1
    return repeat


input_numbers = input("Enter a list of numbers seperated by spaces: ").strip().split(" ")
float_numbers = []
for i in range(len(input_numbers)):
    if input_numbers[i] != "":
        float_numbers.append(float(input_numbers[i]))
print(two_length_run(float_numbers))
