n = int(input("Enter an integer: "))
if n% 2 != 0:
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
        num_digits = len(str(factorial))
    print("Factorial:", factorial)
    print("Number of digits in factorial:", num_digits)
else:
    num_str = str(n)
    if num_str == num_str[::-1]:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
