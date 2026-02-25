class Student():
    def __init__(self, name , roll_no, marks):
        self.__name = None 
        self.__roll_no = None
        self.__marks = None

        # initialize using the methods to reuse validation
        self.getter_name(name)
        self.getter_rollno(roll_no)
        self.getter_marks(marks)

    def getter_name(self, name ):
        self.__name = name 
    
    def getter_rollno(self, roll_no):
        if 1 <= roll_no <= 1000:
            self.__roll_no = roll_no
        else:
            print("ERROR")

    def getter_marks(self , marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("ERROR")


d = Student("Gaurav",55,55)
d.getter_marks(55)                           



    
    

