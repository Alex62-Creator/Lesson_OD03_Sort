a = [38, 27, -13, 43, 3, 9, 82, 27, -5, 10]

# Функция рекурсивного разделения
def merge_sort(arr):
    # Условие выхода: если длина массива будет меньше или равна 1
    if len(arr) <= 1:
        return arr

    # Делим массив на 2 части и рекурсивно вызываем merge_sort для левой и правой половин
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Вызываем функцию merge для объединения двух отсортированных половин
    return merge(left, right)

# Функция слияния
def merge(left, right):
    # Результирующий массив, куда будем сливать элементы
    result = []
    # Указатели на текущие элементы left и right
    i = j = 0

    # Слияние с выбором меньшего элемента:
    # Пока оба указателя i и j в пределах своих массивов:
    while i < len(left) and j < len(right):
        # Если left[i] < right[j], добавляем left[i] в result и сдвигаем i
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        # Иначе добавляем right[j] и сдвигаем j
        else:
            result.append(right[j])
            j += 1

    # Если в left или right остались элементы (один из массивов закончился раньше), добавляем их в конец result
    result.extend(left[i: ])
    result.extend(right[j:])

    # Возвращаем объединенный массив
    return result

# Вызываем merge_sort() и выводим результат
print(merge_sort(a))