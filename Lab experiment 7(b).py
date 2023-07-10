class NegativeValue(Exception):
    pass
try:
    name=input( " Enter your name  : ")
    age=int(input("Enter your age  : "))
    if age<0:
        raise NegativeValue
    marks=[]
    for i in range(0,6):
        mark=float(input("Enter marks scored : "))
        marks.append(mark)
    dict_={"NAME":name,"AGE":age,"MARKS":marks}
    print("DETAILS : \n",dict_)
except NegativeValue:
    print("AGE IS NEGATIVE")

 
