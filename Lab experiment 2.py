def can_obtain_string(str1, str2):
    i = 0
    j = 0

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            j += 1
        i += 1

    return j == len(str2)

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if can_obtain_string(s1, s2):
    print("YES")
else:
    print("NO")
