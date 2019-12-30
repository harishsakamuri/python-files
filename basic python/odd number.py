#odd number
li1=list(map(int,input().split()))
for num in li1:
    if num%2!=0:
        print("odd number :",num)


#even number
obj=list(map(int,input().split()))
for numbers in obj:
    if numbers%2==0:
        print("even number :",numbers)
