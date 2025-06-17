class laptop:
    def __init__(self, company_name, model, price ):
        self.company_name = company_name
        self.model = model 
        self.price = price 
    def information (self):
        print (f"company name : {self.company_name}\nmodel : {self.model}\nprice : {self.price}")
        
# First object
laptop1 = laptop("Mac", "MK256413", "1200$")
laptop1.information()

# Second object
laptop2 = laptop("HP", "Pavilion 15", "850$")
laptop2.information()