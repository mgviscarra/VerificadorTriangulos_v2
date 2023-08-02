def verifyDataInput(value):
    try:
        return float(value) > 0
    except ValueError:
        return False

def verifyTriangle(v1, v2, v3):
    return (v1 + v2) > v3 and (v1 + v3) > v2 and (v2 + v3) > v1

def inputValues(mssg):
    while True:
        value = input(mssg)
        if verifyDataInput(value):
            return float(value)
        else:
            print("Invalid input. Only positive numeric values are allowed.")

def getTriangleType(v1,v2,v3):

    if v1==v2==v3:
        mssg = "The triangle is Equilateral."
    elif v1==v2 or v1==v3 or v3==v2:
        mssg = "The triangle is Isosceles."
    else:
        mssg = "The triangle is Scalene."
    return mssg

while True:
    v1 = inputValues("Enter the first value: ")
    v2 = inputValues("Enter the second value: ")
    v3 = inputValues("Enter the third value: ")
    ##print(f"Values are {v1}, {v2}, {v3}")

    if verifyTriangle(v1, v2, v3):
        print(getTriangleType(v1,v2,v3))
    else:
        print("The input values cannot form a triangle.")
    
    choice = input("Do you want to test another triangle? Other answer different than yes will be considered no: ")
    if choice.lower() != "yes":
        break
