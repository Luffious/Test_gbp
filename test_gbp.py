import csv
import os
import time
from datetime import datetime, timedelta

def task_1():
    '''
    имеется текстовый файл file.csv, в котром разделитель полей с данными: | (верт. черта)
    пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)

    lastname|name|patronymic|date_of_birth|id
    Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
    Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
    ...

    Задание
    1. Реализовать сбор уникальных записей
    2. Случается, что под одиннаковым id присутствуют разные данные - собрать отдельно такие записи

    Returns:
        dict[str, list]: Словарь с уникальными и совпадающими записями
    '''
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


def task_2():
    '''
    в наличии список множеств. внутри множества целые числа
    m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

    Задание: посчитать 
     1. общее количество чисел
     2. общую сумму чисел
     3. посчитать среднее значение
     4. собрать все множества в один кортеж
     *написать решения в одну строку

    Returns:
        dict[str, Any]: Словарь с общим количеством чисел, общей суммой чисел, средним значением и кортежом
    '''
    m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
    num_amount = len([num for sets in m for num in sets])
    total_sum = sum([num for sets in m for num in sets])
    average_value = total_sum / num_amount
    m_to_tuple = tuple([num for sets in m for num in sets])
    return {'num_amount': num_amount, 'total_sum': total_sum, 'average_value': average_value, 'm_to_tuple': m_to_tuple}


def task_3():
    '''
    имеется список списков
    a = [[1,2,3], [4,5,6]]

    Задание:
    сделать список словарей
    b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]

    *написать решение в одну строку

    Returns:
        list[dict[str, int]]]: Список словарей
    '''
    a = [[1,2,3], [4,5,6]]
    b = [dict([(f'k{x + 1}', sublist[x]) for x in range(len(sublist))]) for sublist in a]
    return b


def task_4(path_to_dir: str, N: int):
    '''
    Имеется папка с файлами
    Реализовать удаление файлов старше N дней

    Args:
        path_to_dir (str): Путь к директории с файлами
        N (int): Количество дней для актуальности файла
    '''
    files = [entry.name for entry in os.scandir(path_to_dir) if entry.is_file()]
    days_to_seconds = N * 24 * 60 * 60
    date_of_modification = 0
    for file_path in files:
        full_path = os.path.join(path_to_dir, file_path)
        with open(full_path, 'r'):
            date_of_modification = os.stat(full_path).st_mtime
        if time.time() - days_to_seconds > date_of_modification:
            os.remove(full_path)
    return


def task_5(path_to_file: str):
    '''
    В наличии текстовый файл с набором русских слов(имена существительные, им.падеж)
    Одна строка файла содержит одно слово.

    Задание:
    Написать программу которая выводит список слов, 
    каждый элемент списка которого - это новое слово,
    которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
    Порядок вывода слов НЕ имеет значения

    Args:
        path_to_file (str): Путь к файлу с словами
    '''
    with open(path_to_file, 'r', encoding='utf-8') as f:
        words = []
        index = 1
        print('Выбери слово из списка:')
        for line in f:
            word = line.replace('\n', '')
            words.append(word.lower())
            print(f'{index}) {word}')
            index += 1
        word_index = 0
        while word_index <= 0 or word_index >= index:
            try:
                word_index = int(input('Введи номер слова: '))
                if word_index <= 0 or word_index >= index:
                    print('Нет такого номера')
            except ValueError:
                print('Нет такого номера')
        chosen_word = words[word_index - 1]
        combinded_words = []
        for word in words:
            appended = False
            for index in reversed(range(1, len(word))):
                pos = len(word[:index])
                if word[:index] in chosen_word[-pos:] and not appended:
                    combinded_words.append(f'{chosen_word}{word[pos:]}')
                    appended = True
        print('Список объединённых слов:')
        for combined_word in combinded_words:
            print(combined_word)
    return


task_1_result = task_1()
task_2_result = task_2()
task_3_result = task_3()

# Данный кусок кода требуется для проверки реализации задания 4
# Здесь создаётся 21 файл с датами изменения в диапазоне от 20 дней до текущей даты до текущей даты
current_date = datetime.now()
for i in range(-20, 1):
    path = f'Test Folder/File {i + 21}'
    with open(path, 'w') as f:
        file_date = current_date + timedelta(days=i)
        new_mtime = time.mktime(file_date.timetuple())
        current_mtime = os.stat(path).st_mtime
        os.utime(path, (current_mtime, new_mtime))
task_4_result = task_4(f'Test Folder', 10)
task_5_result = task_5(f'task_5.txt')