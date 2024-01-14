# TODO Напишите функцию find_common_participants
def find_common_participants(str1: str, str2: str, sep: str = ','):
    set1 = set(str1.split(sep))
    set2 = set(str2.split(sep))
    ans = list(set1 & set2)
    ans.sort()
    return ans


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
