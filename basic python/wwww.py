class course:
    name="harish"
    roll=5
    def show (self):
        print(self.name,self.roll)
    def display(self):
        print("hii I am ",self.name,"and my number is",self.roll)
        
guvi=course()
guvi.show()
guvi.name = "Avadi"
guvi.display()
    
class company(course):
    def job (self):
        print(self.name,self.roll)
