def format_name(f_name, l_name):
    h = f_name.title()
    o = l_name.title()
    return f"{h} {o}"


print(format_name(f_name="haRI", l_name="haraN"))


def fn_1(text):
    return text + text


def fn_2(text):
    return text.title()


print(fn_2(fn_1("bye ")))

#multiple return values


def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return
    h = f_name.title()
    o = l_name.title()
    return f"Result: {h}{o}"


#print(format_name(input("what is your first name?"), input("what is your last name?")))

def is_leap_year(year):
    if year % 4 == 0 and year % 400 == 0 and year % 100 == 0:
        return f"True\nThe year {year} is a leap year."
    else:
        return f"False\nThe year {year} is not a leap year."


print(is_leap_year(int(input("Give a year to check, whether it is leap year or not:"))))
