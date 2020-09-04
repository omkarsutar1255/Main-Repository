def searcher():
    import time
    # some 4 seconds time consuming task
    book = "This is a book om omkar and omkar sutar"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)             # to start searcher() funtion
search.send("omkar")            # send values to (yield) function
input("press any key")
search.send("omkar sutar")
input("press any key")
search.send("omkar sutar")
search.close()           # To stop searcher() funtion



def search():
    with open("reading file 1") as f1:
         b1 = f1.read()
    with open("reading file 2") as f2:
        b2 = f2.read()
    with open("reading file 3") as f3:
        b3 = f3.read()

    while True:
        text = (yield)
        if text in b1:
            print("your name is in 1 file")
        if text in b2:
            print("your name is in 2 file")
        if text in b3:
            print("your name is in 3 file")
        else:
            print("your name is not in letters")

abc = search()
next(abc)
print("Enter your name")
name = input()
abc.send(name)