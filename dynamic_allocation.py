class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.phone_no = None

    def allocation(self, n, a, p):
        # Simulating dynamic allocation (not needed in Python, but kept for concept)
        self.name = n
        self.age = a
        self.phone_no = p

    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone Number: {self.phone_no}")

    def deallocate(self):
        # Again, Python does automatic garbage collection, but let's simulate it
        self.name = None
        self.age = None
        self.phone_no = None


# Main code
if __name__ == "__main__":
    obj = Person()
    obj.allocation("Mahima", 18, 9876543210)
    obj.show()
    obj.deallocate()
