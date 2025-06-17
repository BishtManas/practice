class students :
    def __init__(self, name, grade, subject = "Maths" ):
        self.name = name 
        self.grade = grade 
        self.subject = subject
    
    def baccha (self):
        print (f"name : {self.name}\ngrade : {self.grade}\nsubject : {self.subject}")
    
obj = students("Manas" , "A+"  )
obj.baccha()
#you can add multiple students name 
        