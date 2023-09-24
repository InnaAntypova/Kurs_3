import json
from operator import itemgetter
import datetime


def load_operations_json(file_path):
    """
    Функция читает json
    :return: список из словарей
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        temp_file = json.load(file)

        list_operations = []
        for f in temp_file:  # если в списке есть пустой словарь
            if f == {}:
                continue
            else:
                list_operations.append(f)
        return list_operations


def sorted_operations(lst_operations):
    """
    Функция сортирует операции по ключам
    :param lst_operations:
    :return: отсортированный список
    """
    sort_date = sorted(lst_operations, key=itemgetter('date'), reverse=True)
    sort_operations = sorted(sort_date, key=itemgetter('state'), reverse=True)
    return sort_operations


def get_date(i):
    """
    Функция возвращает дату в нужном шаблоне
    """
    date_time_str = i['date']
    date_time_obj = datetime.datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%S.%f")
    date = date_time_obj.date().strftime('%d.%m.%Y')
    return date


