number1=int(input("A First Number Enter : "))
number2=int(input("A Second Number Enter : "))

print("\n")

if(number1>number2):
    largernumber=number1
    smallnumber=number2
else:
    smallnumber=number2
    largernumber=number1

while True:
    division=largernumber//smallnumber
    mod=largernumber%smallnumber
    print(largernumber,"=",smallnumber,".",division,"+",mod)
    if(mod<division):
        print("-"*50)
        print("OBEB : ",smallnumber)
        break
    largernumber=smallnumber
    smallnumber=mod
