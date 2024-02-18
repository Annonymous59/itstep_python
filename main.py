class Student:
    print("Hi")

    def __init__(self,name = None,height = 160):
        self.name = name
        self.height = height

    def __bool__(self):
        return self.name == 1000-7

    def __len__(self):
        return self.height
Sally = Student()


print(Sally.__len__())
print(Sally.__bool__())

