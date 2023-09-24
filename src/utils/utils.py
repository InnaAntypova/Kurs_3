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


def hide_number_from(card_number_from):
    """
    Функция кодирует звездочкой номер карты Отправителя
    """
    hide_number_from_ = card_number_from[0:4] + ' ' + card_number_from[4:6] + '*' * len(card_number_from[6:-4]) + \
                        card_number_from[-4:]
    return hide_number_from_


def hide_number_to(card_number_to):
    """
    Функция кодирует звездочкой номер карты Получателя
    """
    hide_number_to_ = '*' * len(card_number_to[-6:-4]) + card_number_to[-4:]
    return hide_number_to_


def get_feedback(i, date):
    """
    Функция генерирует сообщение с информацией об операциях
    """
    print(f"{date} {i['description']}")
    if 'from' not in i:  # если нет ключа 'from'
        card = i['to'].split()
        card_number_to = card[-1]
        number_to = hide_number_to(card_number_to)
        print(f" > {' '.join(card[:-1])} {number_to}")
    else:
        card = i['to'].split()
        card_number_to = card[-1]
        number_to = hide_number_to(card_number_to)
        card_ = i['from'].split()
        card_number_from = card_[-1]
        number_from = hide_number_from(card_number_from)
        print(f"{' '.join(card_[:-1])} {number_from} > {' '.join(card[:-1])} {number_to}")

    print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
    print(" ")
