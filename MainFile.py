# todo 1) Сформировать массив палиндромов ГОТОВО
# todo 2) написать функцию-проверку числа на полиндром ГОТОВО
# todo 3) написать алгоритм перебора вариантов ГОТОВО
import datetime


def is_palindromic(x):
    x = str(x)
    left = x[0:3]
    right = x[5:2:-1]
    # print(left, right)
    if left == right:
        # print("Число является палиндромом")
        return True


start = datetime.datetime.now()

array = []
first_multiplicator_array = []
second_multiplicator_array = []

for i in range(1, 999):
    for k in range(1, 999):
        multiplication = i * k
        if is_palindromic(multiplication):
            first_multiplicator_array.append(i)
            second_multiplicator_array.append(k)
            array.append(multiplication)

answer = max(array)
index = array.index(answer)

stop = datetime.datetime.now()
time = stop - start

print("Вычисления закончены за ", time.microseconds, "микросекунд.")
print('Максимальное число палиндром, полученное в результате произведения двух 3-хзначных чисел = ', answer)
print("Оно получено произведением: ", first_multiplicator_array[index], "x", second_multiplicator_array[index])