a=input().split()
b=input().split()
key=["name","address"]
value=["harish","tirupathi"]
for i in a:
    if i in key:
        print("ok")
        for j in b:
            if j in value:
                print("ok")
            else:
                print("not ok")
    else:
        print("not ok")
     
        


