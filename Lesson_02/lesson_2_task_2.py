year = int[input("Введите год:")]


def is_year_leap(year):
    if (year % 4 == 0):
        print('год високосный', year, True)
    else:
        print('год не високосный', year, False)


is_year_leap(year)
