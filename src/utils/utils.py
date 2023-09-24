import json


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


