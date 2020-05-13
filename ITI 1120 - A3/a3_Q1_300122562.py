def number_divisible(numbers, divisor):
    """([list],int) -> int
    parses through list of numbers determining how many are divisible by number requested
    preconditions: list of ints,
    """
    total_divisible = 0
    for i in range(len(numbers)):
        if i % divisor == 0:
            total_divisible += 1
    return total_divisible


input_numbers = input("Enter a list of numbers seperated by spaces: ").strip().split(" ")
divide = int(input("How would you like to divide those numbers? ").strip())
numbers = []
for i in range(len(input_numbers)):
    if input_numbers[i] != "":
        numbers.append(float(input_numbers[i]))
print("The # of items divisible by", divide, "is",number_divisible(numbers, divide))
