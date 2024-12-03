age=int(input("Enter your age: "))
weight=int(input("Enter your weight: "))

if age<65 and age>18:
    if weight>40 and weight<80:
        print("Eligible for blood donation!!")
    else:
        print("Inapropriate weight")
else:
    print("inapropriate age")
