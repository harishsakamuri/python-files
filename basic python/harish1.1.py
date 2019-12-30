a=input().split()
b=input().split()
userid=["harish","ramesh","naresh","hari","vinod","surya","jashwanth","tejo"]
password=["latish","naguru","asula","tapel","kumar","teja","jack","verma"]
for m in a:
    if m in userid:
        print("hi")
        for n in b:
            if n in password:
                print("welcome")
            else:
                print("invalid password")
    else:
        print("invalid userid")
                
