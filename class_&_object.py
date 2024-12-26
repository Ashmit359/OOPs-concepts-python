class student :
    college_name = "Chandigarh University"
    name = "anonymoua" #class attr
    
    def __init__(self,name, marks):
        self.name = name # obj attr > class attr 
        self.marks = marks
        print("add new student in database")
    
s1 = student("Ashmit sinha", 99)
print(s1.name,s1.marks)

s2 = student ("Anamika Sinha", 100)
print(s2.name,s2.marks)

print(s2.college_name)
print(s1.college_name)

"""what does this self mean self means which is new  is the object which is being created
i.e. this which  s1 object which we are creating as a new object, this is what we are
calling self, self means myself,this is the reference of the object on whose creation the
constructor is called,means it is pointing towards this,"""