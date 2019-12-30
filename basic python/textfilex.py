f = open("harish_data.txt","w")
f.write("name harish\n")
f.write("dept ece\n")
f.write("sec c\n")
f.close()
f = open("harish_data.txt","r")
dit = {}
for values in f:
    us,pd = values.split()
    dit[us] = pd
print(dit)    
    
    
    
    
    
    
    

    
    


