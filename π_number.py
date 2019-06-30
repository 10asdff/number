n=0
sum=0
finall=1000000   #You can change the number for better result

while n<finall:
    sum=sum+((-1)**n)/(2*n+1)
    n=n+1

print("Pi sayısının değeri : ",4*sum)