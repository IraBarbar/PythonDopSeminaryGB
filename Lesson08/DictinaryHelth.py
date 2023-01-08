# 3: Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# Поэкспериментируйте с значениями урона и жизней по желанию.
# ### Теперь надо создать функцию attack(person1, person2).

# ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего
# и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.
import random
person_1 = \
    {
        'name': '',
        'health': 100,
        'damage': 50,
        'armor': 0

    }
person_2 = \
    {
        'name': '',
        'health': 100,
        'damage': 50,
        'armor':  0
    }

person_1['name'] = input('Имя игрока №1 : ')
person_2['name'] = input('Имя игрока №2 : ')

count = 0
while count < 10:
    person_damage = \
        {
            1: '- голова',
            2: '- нога',
            3: '- рука',
            4: '- живот',
            5: '- спина'
        }
    person_armor = \
        {
            1: 'защита головы',
            2: 'защита ноги',
            3: 'защита руки',
            4: 'защита живота',
            5: 'защита спины'
        }

    def print_attack(dic_1, dic_2):
        while True:
            print(
            f'{dic_1["name"]} атакует. Выберите куда {dic_1["name"]} ударит: ')
            for item in dic_2.items():
                print(*item)
            x = int(input())
            if x in range(1,6):
                break
        return x
            
    x = print_attack(person_1,person_damage)
    y = print_attack(person_2,person_damage)

    def armor(dic_1,dic_3,n):
        z = random.randint(1, 5)
        input(f'{dic_1["name"]} вам выпол бонус - {dic_3[z]} !')
        if n == z:
            n = 0
        else:
            n = random.randint(1,50)
        dic_1['armor'] = dic_3[z]
        return n

    y = armor(person_1,person_armor,y)
    x = armor(person_2,person_armor,x)

    person_2['health'] = person_2['health'] - x
    person_1['health'] = person_1['health'] - y
    print()
    
    if person_1['health'] > person_2['health']:
        print(f'Победитель {person_1["name"]}!')
        if person_2['health'] < 0:
            print(
                f'{person_2["name"]}, вас убили :(\n Конец игры!')
            break
        print(
            f'{person_1["name"]} остаток жизни {person_1["health"]}\n{person_2["name"]} остаток жизни {person_2["health"]} ')
      
    elif person_1['health'] == person_2['health']:
        print(f'Ничья :)')
    
    else:
        print(f'Победитель {person_2["name"]}!')
        if person_1['health'] < 0:
            print(
                f'{person_1["name"]}, вас убили :(\n Конец игры!')
            break
        print(
            f'{person_1["name"]} остаток жизни {person_1["health"]}\n{person_2["name"]} остаток жизни {person_2["health"]} ')
    print()
    count = count + 1 