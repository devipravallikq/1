class placements:
 def info(self):
  print("1062")
class dept(placements):
 def display(self):
  print("all dept")
class pragati(dept):
 def welcome(self):
  print("welcome")
obj2=pragati()
obj2.info()

class SubjMarks:
 math=int(input("enter the marks of math"))
 DE=int(input("enter the marks of the DE"))
 c=int(input("enter the marks of c"))
 english=int(input("enter the marks of english"))
class PractMarks:
    cpract=int (input ("Enter practicals marks of cpract"))
class Result(SubjMarks,PractMarks): 
    def total(self):
        if self.math>40 and self.DE>40 and self.c>40:
            print("pass")
        else:
            print("fail")

obj=Result()
obj.total()

