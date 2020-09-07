class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"name is {self.name}, salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        list = string.split("-")
        """return cls(list[0], list[1], list[2])"""
        return cls(*list)

    @staticmethod
    def printgood(string):
        print("this is " + string)

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"name is {self.name}, game is {self.game}"

class Coolprogrammer(Employee, Player):        # use variables from ordered class
                                               # (first from employee then player then coolprogrammer)
    var = 10
    language = "c++"
    def printlanguage(self):
        print(self.language)

omkar = Employee("omkar", 50000, "student")
avdhut = Employee("rohan", 40000, "friend")

shubham = Player("shubham", ["cricket"])
karan = Coolprogrammer("karan", 7500, "coolprogrammer")
karan.printlanguage()
print(karan.printdetails())
print(karan.var)       # var variable first check in Coolprogrammer class then Employee class and Player class