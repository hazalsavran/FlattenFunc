# 1. Ödev: Listeyi Düzleştiren Fonksiyon
def flatten(lst):
    flattened_list = []
    for item in lst:
        if isinstance(item, list):
            flattened_list.extend(flatten(item))  # İç içe listeleri düzleştir
        else:
            flattened_list.append(item)
    return flattened_list

input_list = [1, [2, [3, 4], 5], ['a', 'b', ['c', 'd']]]
flattened = flatten(input_list)
print("Düzleştirilmiş Liste:", flattened)

# 2. Ödev: Listeyi Tersine Döndüren Fonksiyon
def reverse_nested_list(lst):
    reversed_list = []
    for item in lst:
        if isinstance(item, list):
            reversed_list.append(reverse_nested_list(item))
        else:
            reversed_list.append(item)
    return reversed_list[::-1]

input_list_2 = [[1, 2], 3, [[4, 5], 6], 7]
reversed = reverse_nested_list(input_list_2)
print("Tersine Döndürülmüş Liste:", reversed)
