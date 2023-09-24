from utils.utils import load_operations_json,sorted_operations,get_date,get_feedback
import os.path

# Путь к файлу c операциями
json_path = os.path.join('data', 'operations.json')


#Основной код
def main():
    operations = load_operations_json(json_path)
    sort_operations = sorted_operations(operations)
    for i in sort_operations[:5]:
        date = get_date(i)
        view_operations = get_feedback(i, date)
    return view_operations


if __name__ == '__main__':
    file_path = json_path
    main()
