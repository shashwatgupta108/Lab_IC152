class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.courses = set(['MA101'])
        self.enrol()
        print(self.name)
        print(self.rollno)
        for x in self.courses:
            print(x, end=',')

    def enrol(self):
        x = input("Course List: ")
        a = set(x.split(' '))
        self.courses = self.courses.union(a)


if __name__ == "__main__":
    Name = input("Enter Name: ")
    RollNo = input(("Enter Roll No.: "))
    b = Student(Name, RollNo)
