a=input().split()
count=0
for p in a:
    if p=="traditionally":
        print("found")
    else:
        count=count+1
        if count==len(a):
            print("not found")

