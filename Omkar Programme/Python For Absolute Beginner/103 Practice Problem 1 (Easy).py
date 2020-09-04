while True:
    ans = input("Enter your age or date of birth : ")
    len1 = len(ans)
    if len1 < 4:
        age = int(ans)
        if age < 1:
            print("your are not born yet")
        elif (age > 1 and age < 7) or (age > 100):
            print("you can't use computer")

        elif age < 100 and age > 80:
            print("you are oldest person alive\n", 100-age, "years are left for century")
        else:
            print("you born in year :", 2020-age, "\n", 100-age, "years are left for century")
        ans2 = input("Enter e to Exit")
        if ans2 == "e":
            break

    elif len1 == 4:
        DOB = int(ans)
        age = 2020 - DOB
        if age < 1:
            print("your are not born yet")
        elif (age > 1 and age < 7) or (age > 100):
            print("your age is :", age, "\nyou can't use computer")

        elif age < 100 and age > 80:
            print(age, "\nyou are oldest person alive\n", 100-age, "years are left for century")
        else:
            print("your age is :", age, "\n", 100-age, "years are left for century")
        ans2 = input("Enter e to Exit")
        if ans2 == "e":
            break
    else:
        ans2 = input("Run again and Enter correct ans\nEnter e to Exit")
        if ans2 == "e":
            break