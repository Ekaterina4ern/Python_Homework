year = int(input("Введите год:"))

def is_year_leap():
    if (year % 4 ==0):
        print(True)
    else: print(False)
is_year_leap()


def is_year_leap(year):
        if (year % 4 == 0):
            print('год високосный', year, True)
        else:
            print('год невисокосный', year, False)
is_year_leap(year)