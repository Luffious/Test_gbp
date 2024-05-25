import csv

def task_1():
    '''Задание №1'''
    with open('file.csv', 'r', newline='', encoding='utf-8') as file:
        next(file)
        unique_data, similar_data, id_s, bad_id_s = [], [], [], []
        reader = csv.reader(file, delimiter='|')
        for line in reader:
            person = {'lastname': '', 'name': '', 'patronymic': '', 'date_of_birth': '', 'id': ''}
            field_num = 0
            for key in person:
                person[key] = line[field_num].replace(' ', '')
                field_num += 1
            if person['id'] in id_s:
                similar_data.append(person)
                bad_id_s.append(person['id'])
            else:
                unique_data.append(person)
            id_s.append(person['id'])
    bad_indicies = []
    for index in range(len(unique_data)):
        if unique_data[index]['id'] in bad_id_s:
            similar_data.append(unique_data[index])
            bad_indicies.append(index)
    bad_indicies.reverse()
    for index in range(len(bad_indicies)):
        unique_data.pop(index)
    similar_data = sorted(similar_data, key=lambda d: d['id'])
    return {'unique_data': unique_data, 'similar_data': similar_data}


# имеется текстовый файл file.csv, в котром разделитель полей с данными: | (верт. черта)
# пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)

"""
lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
...
"""

# Задание
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одиннаковым id присутствуют разные данные - собрать отдельно такие записи
result = task_1()
pass