mounth = int(input('введите номер месяца: '))

def month_to_season():
    if mounth in [12, 1, 2]:
        print("Зима")

    if mounth in [3, 4, 5]:
        print("Весна")

    if mounth in [6,7,8]:
        print("Лето")

    if mounth in [9,10,11]:
        print("Осень")
    else:
        print("Некорректный номер месяца")

month_to_season()