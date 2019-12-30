b = list(input())
count=0
for i in b:
    if i=="f":
        print("found")
    else:
        count=count+1
        if count==len(b):
            print("not found")
