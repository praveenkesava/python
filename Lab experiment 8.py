try:
    file="sample.txt"
    files=open(file,'r')
    n=int(input("Enter the lines to be read  : "))
    for i in range(0,n):
        a=files.readline()
        line=a.strip()
        if len(line)!=0:
            print(line)
        else:
            break
except FileNotFoundError:
    print("FILE NOT FOUND.....")


