number=int(input("Enter a number please : "))
i=2

while i<number:
    if(number%i==0):
        print("Number is not prime")
        break
    i=i+1
else:
    print("Number is prime")
