#lab2
def temperature(enter):
    correct = []
    sum = 0
    for element in enter:
        if type(element) != str:
            sum += element
            correct.append(element)
    average_temp = round(sum / len(correct), 2)
    print("The average temperature is {0}\u00b0C.".format(average_temp))

enter = []
vvod = int(input("Введите, сколько фиксаций было"))
for element in range(vvod):
    edin_vvod = input()
    if edin_vvod != "None":
        enter.append(int(edin_vvod))
    else:
        enter.append(str(element))
temperature(enter)

print("The second task")

def second(enter):
    negative = []
    non_negative = []
    for element in enter:
        if element < 0:
            negative.append(element)
        else:
            non_negative.append(element)
    negative.sort(reverse=True)
    non_negative.sort()
    print("Список отрицательных значений: {0}.".format(tuple(negative)))
    print("Cписок неотрицательных значений: {0}.".format(tuple(non_negative)))
enter = [int(i) for i in input('Введите значения цен через пробел ').split()]
second(enter)

print("The third task!")
a = int(input("Choose your a"))
b = int(input("Choose your b"))
def exponentiation(chislo, stepen):
    result = chislo ** stepen
    print("The result of exp of {0} by {1} is {2}.".format(chislo, stepen, result))
exponentiation(a, b)

def rekursia(chislo, stepen):
    if stepen == 0:
        return 1
    return chislo * rekursia(chislo, stepen - 1)
answer = rekursia(a, b)
print("The result of rek.exp is {0}.".format(answer))
