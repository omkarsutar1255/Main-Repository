a = input("whats your name")
b = input("How much do you earn")
if int(b) == 0:
    raise ZeroDivisionError("b is o so stopping the programme")
if a.isnumeric():
    raise Exception("Numbers are not allowed")   # if condition false further will not execute

print(f"hello {a}")


c = input("Enter your name")
try:
    print(a)

except Exception as e:
    if c== "omkar":
        raise ValueError("omkar is not allowed")
    print("Exception handled")