class student :
    college_name = "Chandigarh University"
    name = "anonymoua" #class attr
    
    def __init__(self,name, marks):
        self.name = name # obj attr > class attr 
        self.marks = marks
        
    def welcome (self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks    
            
    
s1 = student("Ashmit sinha", 99)
s1.welcome()
print(s1.get_marks())





