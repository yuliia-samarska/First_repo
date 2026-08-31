# Методи, що використовуються у роботі зі списками

# .append() - додає елемент у кінець списку
my_list = [1, 2, 3]
my_list.append(4)
# print(my_list)  Виведе: [1, 2, 3, 4]

# .remove() - видаляє перше входження елемента зі списку
# my_list.remove("Hello") Видаляє перше входження "Hello" зі списку

# У Python синтаксис доступу за індексом виглядає так:
some_iterable = ["a", "b", "c"]
first_letter = some_iterable[0]
middle_one = some_iterable[1]
last_letter = some_iterable[2]

# Python підтримує індексування елементів з кінця.
# Перший елемент з кінця має індекс -1.

some_iterable = ["a", "b", "c"]
first_letter = some_iterable[-3]
middle_one = some_iterable[-2]
last_letter = some_iterable[-1]

#Змінимо другий елемент списку some_iterable на -2. Другий елемент списку має індекс 1, а отже:
some_iterable[1] = -2

# Метод .pop() видаляє елемент за індексом і повертає його значення. Якщо індекс не вказано, видаляється останній елемент.
chars = ['a', 'b', 'c']
last = chars.pop(1)
# print(chars)  Виведе: ['a', 'c']

# Метод .extend() додає всі елементи з іншого списку в кінець поточного списку.
chars = ['a', 'b', 'c']
numbers = [1, 2]
chars.extend(numbers)
# print(chars)  Виведе: ['a', 'b', 'c', 1, 2]

# Метод .insert() вставляє елемент у список за вказаним індексом.
chars = ['a', 'b', 'c']
chars.insert(1, 'x')
# print(chars)   Виведе: ['a', 'x', 'b', 'c']

# Метод .clear() видаляє всі елементи зі списку.
chars = ['a', 'b']
chars.clear() # []
# print(chars)  Виведе: []

# Метод .index() повертає індекс першого входження елемента у списку.
chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c')
# print(c_ind)  Виведе: 2

# Метод .count() повертає кількість входжень елемента у списку.
my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
# print(count_2)  Виведе 4, оскільки число 2 зустрічається 4 рази
# Якщо елемент відсутній у списку, count() поверне 0.

# Метод .sort() сортує елементи списку в порядку зростання або спадання.
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
# print(nums)  Виведе [1, 1, 2, 3, 4, 5, 9]

words = ["banana", "apple", "cherry"]
words.sort(key=len)
# print(words)  Виведе ['apple', 'banana', 'cherry'], оскільки сортування відбувається за довжиною рядків.

# Слід пам'ятати, що метод sort() змінює сам список, на якому він був викликаний. Якщо потрібно зберегти початковий порядок елементів, розгляньте можливість створення копії списку перед сортуванням або використай функцію sorted().

# Функція sorted() повертає новий відсортований список, не змінюючи оригінальний.
nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
# print(sorted_nums)  Виведе [1, 1, 2, 3, 4, 5, 9]

# Метод також використовує аргумент reverse=True, щоб відсортувати об'єкти у зворотному порядку.
sorted_nums_desc = sorted(nums, reverse=True)
# print(sorted_nums_desc)  Виведе [9, 5, 4, 3, 2, 1, 1]

# За допомогою аргументу key можна вказати функцію, яка буде застосовуватися для визначення порядку сортування.
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
# print(sorted_words)  Виведе ['apple', 'banana', 'cherry']

# Функція len() повертає кількість елементів у списку.
my_list = [1, 2, 3, 4, 5]
# print(len(my_list))  Виведе 5, оскільки у списку 5 елементів

# Метод .copy() створює поверхневу копію списку.
chars =  ['a', 'b']
chars_copy = chars.copy()
# print(chars_copy)  Виведе ['a', 'b']

# Метод .reverse() змінює порядок елементів у списку на зворотний.
chars = ["banana", "apple", "cherry"]
chars.reverse()
# print(chars)  Виведе ['cherry', 'apple', 'banana']

