def find_occurrence(numbers, target):
    positive = []
    negative = []
    count = 0

    for i in range(len(numbers)):
        if numbers[i] == target:
            positive.append(i)
            negative.append(-len(numbers) + i)
            count += 1

    return count, positive, negative

numbers = list(map(int, input("Enter the list of numbers :")))
target = int(input("Enter the element to be found: "))
occurrence, positive, negative = find_occurrence(numbers, target)
print("Element", target, "occurs", occurrence, "time(s) in the list.")
print("Positive Index:", ", ".join(map(str, positive)))
print("Negative Index:", ", ".join(map(str, negative)))
