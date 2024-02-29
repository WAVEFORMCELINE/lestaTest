# ---------- Задание 1 ----------
# Функция из задания
# def isEven(value):
#     return value % 2 == 0

def isEven(value):
    return value & 1 == 0

print(isEven(1)) #False
print(isEven(2)) #True
# Предложенный мной вариант может быть более эффективен в производительности и использовании памяти,
# так как использует битовую операцию вместо операции деления.
#

# ---------- Задание 2 ----------
# Первый класс FIFO
class Fifo1:
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        return item

# Плюсы:
# 1. Простая и понятная реализация: код короткий и легко понимаемый.
# 2. Для определения индексов в массиве использовуется операция %,
# что позволяет обеспечить непрерывную работу циклического буфера.
#
# Минусы:
# 1. Ограничение на количество элементов в буфере из-за фиксированного размера массива.
# 2. Возможно переполнение буфера при многократных операциях добавления элементов без удаления.

# Второй класс FIFO
class Fifo2:
    def __init__(self, size):
        self.buffer = []
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        if len(self.buffer) < self.size:
            self.buffer.append(item)
            self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if len(self.buffer) > 0:
            item = self.buffer[self.head]
            self.head = (self.head + 1) % self.size
            return item
# Плюсы:
# 1. Гибкость размера буфера: буфер будет увеличиваться по мере добавления элементов и уменьшаться по мере их удаления.
# 2. Отсутствие верхнего предела количества элементов в буфере.
#
# Минусы:
# 1. Динамическое управление размером буфера может привести к увеличению затрат памяти и времени на управление данными.
# 2. Неоптимальное использование памяти при добавлении и удалении элементов.

# Первый вариант Fifo1 более производителен при работе с большими буферами из-за использования операции % для определения индексов.
# Однако, при малом размере буфера или небольшом количестве операций добавления/извлечения, разница в производительности может быть незначительной.

# Второй вариант Fifo2 имеет возможность быть более гибким с точки зрения управления памятью.
# Однако, при управлении размером буфера и индексацией элементов может потреблять больше ресурсов.

# ---------- Задание 3 ----------
# Пирамидальная сортировка
# Пирамидальная сортировка (Heap Sort) имеет сложность O(n log n), то есть время выполнения растёт логарифмически пропорционально количеству элементов
# Алгоритм не меняет порядок равных элементов, то есть он устойчив.

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)

arr = [5, 14, 2, 3, 50, 5, -47]
heapSort(arr)
n = len(arr)
print('Результат сортировки:')
for i in range(n):
    print(arr[i])

