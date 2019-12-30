a = int(input())
n = (a*2)-1

for i in range(1,n+1):
    for j in range(1,n+1):
        if (i == 2 or i == n):
            print(a,end="")
        elif (i == 2 or i == n-1):
            print(a)
