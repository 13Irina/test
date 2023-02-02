#13.8
def bill(a):
    age = []
    price = []
    while a > 0:
        y = int(input("Введите возраст: "))
        age.append(y)
        a -= 1
    for i in range(len(age)):
            if age[i] < 18:
                a = 0
                price.append(a)
            elif 18 < age[i] < 25:
                a = 990
                price.append(a)
            else:
                a = 1390
                price.append(a)
    if len(price) == 1 and price[0] == 0:
        return 0
    elif sum(price) == 0:
        return 0
    else:
        summ = sum(price)
        return summ


how_many = int(input("Введите количество билетов: "))

if 0 < how_many < 4:
    b = bill(how_many)
    if b == 0:
        print("Поздравляем! У Вас бесплатный билет!")
    else:
        print("Сумма к оплате: ", b)
elif how_many > 3:
    b = bill(how_many)
    if b == 0:
        print("Поздравляем! У Вас бесплатный билет!")
    else:
        print("Сумма к оплате: ", b-b*0.1)
else:
    print("Вы ввели некорректное число!")