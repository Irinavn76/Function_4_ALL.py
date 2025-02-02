# Функция наибольшего числа.
def max_number(a, b):
    if a <= b:
        return b
    else:
        return a


# "Пустая" функция
def empty_function():
    pass  # Код будет добавлен позже


# Генератор четных чисел
def even_numbers(n):
    for a in range(n):
        if a % 2 == 0:
            yield a


# Автотест для функции max_number() из первого задания
def test_max_number():
    assert max_number(20, 2) == 20, "Ошибка: число 20 больше числа 2"
    assert max_number(-10, -6) == -6, "Ошибка: отрицательное число -6 больше отрицательного числа -10"
    assert max_number(55, 55) == 55, "Ошибка: наибольшее число 55"
    assert max_number(88, 99) == 99, "Ошибка: число 99 больше числа 88"


test_max_number()

# Вывод наибольшего числа из чисел 1 и 10.
print(max_number(1, 10))


# Задаем фактическое значение диапазону n.
for a in even_numbers(31):


# Печатаем четные числа
        print("Четным числом в списке является: ", a)



# Выводим автотест
print(max_number(20, 2))
print(max_number(-10, -6))
print(max_number(55, 55)) # AssertionError: Числа равны!
print(max_number(88, 99))
print("Все тесты пройдены!")