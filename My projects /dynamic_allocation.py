class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.phone_no = None

    def allocation(self, n, a, p):
        self.name = n
        self.age = a
        self.phone_no = p

    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone Number: {self.phone_no}")

    def deallocate(self):
        self.name = None
        self.age = None
        self.phone_no = None

if __name__ == "__main__":
    obj = Person()
    obj.allocation("Mahima", 18, 9876543210)
    obj.show()
    obj.deallocate()
