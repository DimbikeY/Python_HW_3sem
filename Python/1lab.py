import random

print("The first task!")
cost =[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
price = [element * 1.2 for element in cost]
print("The new element list: {0}.".format(list(price)))

print("The second task!")
goods = ["milk", "cereal", "potato", "bread", "juice", "carrot", "onion", "cheese", "pasta", "chicken"]
price = [50, 70, 35, 40, 50, 70, 28, 500, 100, 250]
id_staff = [323, 525, 323, 731, 323, 731, 525, 731, 731, 323]
zip_func = zip(goods, price, id_staff)
print("Zip function in use:")
print(list(zip_func))

print("The third task!")
number = int(input("Write your number = "))
from_1_to_100 = []
for element in range(100):
    from_1_to_100.append(random.randint(1, 100))
new_list = ["High" if number > element else "Low" for element in from_1_to_100]
print(new_list)
full_name = ["Анастасия", "Анна", "Мария", "Елена", "Дарья", "Алина", "Ирина", "Екатерина", "Арина", "Полина"
"Ольга", "Юлия", "Татьяна", "Наталья", "Виктория", "Елизавета", "Ксения", "Милана", "Вероника", "Алиса",
"Валерия", "Александра", "Ульяна", "Кристина", "София", "Марина", "Светлана", "Варвара", "Софья", "Диана",
"Яна", "Кира", "Ангелина", "Маргарита", "Ева", "Алёна", "Дарина", "Карина", "Василиса", "Олеся",
"Аделина", "Оксана", "Таисия", "Надежда", "Евгения", "Элина", "Злата", "Есения", "Милена", "Вера",
"Александр", "Дмитрий", "Максим", "Сергей", "Андрей", "Алексей", "Артём", "Илья", "Кирилл", "Михаил",
"Никита", "Матвей", "Роман", "Егор", "Арсений", "Иван", "Денис", "Евгений", "Даниил", "Тимофей",
"Владислав", "Игорь", "Владимир", "Павел", "Руслан", "Марк", "Константин", "Тимур", "Олег", "Ярослав",
"Антон", "Николай", "Глеб", "Данил", "Савелий", "Вадим", "Степан", "Юрий", "Богдан", "Артур",
"Семен", "Макар", "Лев", "Виктор", "Елисей", "Виталий", "Вячеслав", "Захар", "Мирон", "Дамир"]
full_name.sort()
first_list = []
second_list = []
alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
for element in range(len(full_name)):
    for letter in alphabet[14:]:
        if full_name[element][0] == letter:
            first_list = full_name[:element]
            second_list = full_name[element:]
            print("a_m")
            print(first_list)
            print("n_z")
            print(second_list)
    if len(first_list) + len(second_list) == len(full_name):
        break

print("The last one!")
print("Write size of list. Press 'Enter'. Then you have to enter some number.")
list_4 = []
n = int(input())
for i in range(n):
    new_element = int(input())
    list_4.append(new_element)
new_spisok = []
for element in list_4:
    if element < 10:
        new_spisok.append(element * 1.13)
    elif element > 10:
        new_spisok.append(element * 0.18)
    else:
        new_spisok.append(element)
new_spisok.sort()
new_new_spisok = [round(element, 2) for element in new_spisok]
print(new_new_spisok)
with open("file.txt", "w") as file:
    file.write(str(new_new_spisok))

print("\nThe end!")
