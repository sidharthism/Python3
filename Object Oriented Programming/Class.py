class A:
    # Constructor of class
    def __init__(self, a):
        self.a = a

    # Destructor for class
    def __del__(self,):
        print("destructor of class")

a = A(7)
del a