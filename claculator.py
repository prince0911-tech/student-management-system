def calculator(a,b,operation):
    ans=0
    if operation == "+":
        ans=a+b
        print("Ans =",ans)
    elif operation == "-":
        ans=a-b
        print("Ans =",ans)
    elif operation == "*":
        ans=a*b
        print("Ans =",ans)
    elif operation == "/":
        ans=a/b
        print("Ans =",ans)
    else:
        print("Invalid Operation")

a=int(input("Enter one number : "))
b=int(input("Enter sencond number : "))
operation=input("enter operator : ")

calculator(a,b,operation)