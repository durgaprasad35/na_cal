def series():
    return (resistor1 + resistor2)
def parallel():
    return ((1/resistor1) + (1/resistor2))
def operations():
    if operation == "1":
        print((series()))
    elif operation == "2":
       print(parallel())

resistor1 = int(input("Enter your first resistor value : "))
operation = input("choose your operator : ")
resistor2 = int(input("Enter your resistor 2 value : "))
answer = operations()
permisssion = input("Enter yes to continue no to terminate : ")
if permisssion == "yes":
    resistor1 = answer
    operation = input("choose your operator : ")
    resistor2 = int(input("Enter your resistor 2 value : "))
    operations()
    
else:
    print("Thank for using me!!")