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

'''
Python-pip will automatically create the constructor for us If we need our own constructor The constructor is basically
for initialization of the object i.e. if at the time of creating the objectIf  You want to do some work like if
we want to create some new attributes then we do that work inside the constructor.This is how we define our constructor. There are
two types of constructors,default and parameterized. Always first inside the constructor.  Our parameter is the self parameter
which means the object instance and after that we can take different parameters and we can create our own attributes. There are two types of attributes, one
is class attributes and the other is object attributes.  Apart from this, we create our methods inside the class. The functions that are inside the class are
called methods. Inside the methods, we are always writing self. These methods are the functions of our class,
like this is mine.  The first method is done, in the same way we could have created a student object s2, for
that we could have called our method again'''




