class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printdetails(self):
        print("Name:",self.name,"Age:",self.age)
    @staticmethod
    def welcome():
        print("welcome to our glug")
o1=student("Ragu",19)
o1.printdetails()
o1.welcome()
o2=student("pathi",20)
o2.printdetails()
o2.welcome()
