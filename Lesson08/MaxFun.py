# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
nums=[]
for i in range(3):
    nums.append(int(input('Input a numbr: ')))
print(f'Maximum number is {max(nums)} . ')
