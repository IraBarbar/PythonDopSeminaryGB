# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а),
# проживает в городе Москва»
get_person=\
    {
        'name':'',
        'age' :'',
        'city':'',
    }

get_person['name'] = input('Как вас зовут: ')
get_person['age'] = input('Сколько вам лет: ')
get_person['city'] = input('В каком городе вы проживаете: ')

# def person (**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)

print(get_person['name']+ ', ' + get_person['age'] + ' год, проживает в городе '+ get_person['city'] + '.')