myli = [2,3,28,0,7]
string2 = "going tobr goa"
count=0
print(len(string2))
print(len(myli))
for k in range(len(myli)):
    if myli[k]==11:
        print("found")
        break
    else:
        count=count+1
        if count==len(myli):
            print("not found")
print(count)

for l in range(len(string2)):
    if string2[l]=="j":
        print("found")
        break
    else:
        count=count+1
        if count==len(string2):
            print("not found")
print(count)              
