# 2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013. 
# Ваша задача — вывести дату в текстовом виде, например: 
# второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)
mesiac = \
    {
        '01':'января',
        '02':'февраля',
        '03':'марта',
        '04':'апреля',
        '05':'мая',
        '06':'июня',
        '07':'июля',
        '08':'августа',
        '09':'сентября',
        '10':'октября',
        '11':'ноября',
        '12':'декабря',

    }
day = \
    {
        '01':'первого',
        '02':'второго',
        '03':'третьего',
        '04':'четвертого',
        '05':'пятого',
        '06':'шестого',
        '07':'седьмого',
        '08':'восьмого',
        '09':'девятого',
        '10':'десятого',
        '11':'одиннадцатого',
        '12':'двенадцатого',
        '13':'тринадцатого',
        '14':'четырнадцатого',
        '15':'пятнадцатого',
        '16':'шестадцатого',
        '17':'семьнадцатого',
        '18':'восемьнадцатого',
        '19':'девятьнадцатого',
        '20':'двадцатого',
        '21':'двадцать первого',
        '22':'двадцать второго',
        '23':'двадцать третьего',
        '24':'двадцать четвертого',

    }
day_user = []
day_user = input('Введите дату: ').split('.')
print(day_user)

print(day[day_user[0]] ,mesiac[day_user[1]], day_user[2], 'года')