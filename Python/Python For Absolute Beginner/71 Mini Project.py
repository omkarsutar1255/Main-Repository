class Library:

    def __init__(self, lbname, lst):
        self.libraryname = lbname
        self.listofbooks = lst

    def display(self):
        return f"books in {self.libraryname} are\n{self.listofbooks}"

    @staticmethod
    def add(bookname):
        lst.append(bookname)

    @staticmethod
    def lend(bookname):
        lst.remove(bookname)


lst = ["hp1", "hp2", "hp3", "hp4"]
omkarlibrary = Library("omkar's library", lst)
dictionary = {}

while True:
    print("press 1 for display books\npress 2 for lend book\npress 3 for return book"
          "\npress 4 for add book\npress 5 for see who lends book")

    try:
        ans1 = int(input())
    except Exception as e:
        print("retry sir")
        continue

    if ans1 == 1:
        print(omkarlibrary.display())
        ans4 = input("y for back and n for exit")
        if ans4 == "n":
            break
        else:
            continue

    elif ans1 == 2:
        ans2 = input("Enter book name")
        ans3 = input("Enter your name")
        try:
            omkarlibrary.lend(ans2)
            dictionary[ans2] = ans3

        except Exception as e:
            print("Sry book not available")
            print("lender of", ans2, "book is", dictionary.get(ans2))
            ans4 = input("y for back and n for exit")
            if ans4 == "n":
                break
            else:
                continue

    elif ans1 == 3:
        ans2 = input("Enter book name")
        ans3 = input("Enter your name")
        omkarlibrary.add(ans2)
        del dictionary[ans2]
        ans4 = input("y for back and n for exit")
        if ans4 == "n":
            break
        else:
            continue

    elif ans1 == 4:
        ans2 = input("Enter book name")
        ans3 = input("Enter your name")
        omkarlibrary.add(ans2)
        ans4 = input("y for back and n for exit")
        if ans4 == "n":
            break
        else:
            continue

    elif ans1 == 5:
        print(dictionary)
        ans4 = input("y for back and n for exit")
        if ans4 == "n":
            break
        else:
            continue
    else:
        print("enter upto 5")