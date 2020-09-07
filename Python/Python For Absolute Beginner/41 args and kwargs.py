def funargs(normal, *args, **kwargs):    # first normal arguments then args then kwargs
    print(normal)
    for items in args:
        print(items)

    print("\nthis are the close one")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

normal = "I am a normal argument and the students are: "        # normal argument
har = ["omkar", "tufan", "avdhut", "shubham", "akshay"]         # *args argument
kw = {"omkar":"programmer", "avdhut":"engineer", "akshay":"business"}    # **kwargs argument
funargs(normal, *har, **kw)    # first normal arguments then args then kwargs