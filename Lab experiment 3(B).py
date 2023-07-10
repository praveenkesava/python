def is_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

num = list(map(int,input("Enter the list of numbers:")))
if is_ascending(num):
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")
