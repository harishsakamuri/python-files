email = input()
pwd = input()
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
spcl = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
spcl = list(spcl)
print(spcl)
for k in email:
    if k == "@":
        i = email.index(k)
        for s in range(i,len(email)):
            if email[s] == ".":
                print("valid mailid")
                for l in pwd:
                    if l.isupper():
                        a = a+1
                    if l.islower():
                        b = b+1
                    if l.isdigit():
                        c = c+1
                    if (a and b and c) > 0:
                        break
                for h in spcl:
                    if h in pwd:
                        e = e+1
                if(( 5 < len(pwd) <15) and ((a and b and c and e) > 0)):
                    print("valid passwor")
                else:
                    print("invalid password")
            else:
                f = f+1
                if f == (len(email)-i):
                    print("invalid userid")
