# TODO Напишите функцию find_common_participants
def find_common_participants(first_group,second_group,splitter=','):
    set_1 = set(first_group.split(splitter))
    set_2 = second_group.split(splitter)
    together = list(set_1.intersection(set_2))
    together.sort()
    return together


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '_'))