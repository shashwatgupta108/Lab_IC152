class IC152:
    def __init__(self, name, rollno, marks):
        try:
            assert (rollno[:3] == "B21" and len(rollno) == 6)
            assert (marks in range(101))
            self.name = name
            self.rollno = rollno
            self.marks = marks
            if marks >= 40:
                print("pass")
            else:
                print("fail")
        except AssertionError:
            print("Invalid Input")


Name = input("Enter your name: ")
RollNo = input("Enter your rollno: ")
Marks = int(input("Enter your marks: "))
a = IC152(Name, RollNo, Marks)
