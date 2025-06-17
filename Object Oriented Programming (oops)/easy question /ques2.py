class cars:
    def start_engine(self , name):
        self.name = name 
        print (f"{name}->Engine started ")
cars1 = cars()
cars1.start_engine("BMW")