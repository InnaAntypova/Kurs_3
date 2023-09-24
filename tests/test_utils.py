import pytest
from src.utils.utils import load_operations_json, hide_number_from, hide_number_to, sorted_operations, get_date
import os.path

test_json_path = os.path.join('tests', 'data', 'test_operations.json')


@pytest.fixture
def data():
    expected_data = [{"id": 667307132,
                      "state": "EXECUTED",
                      "date": "2019-07-13T18:51:29.313309",
                      "operationAmount": {
                          "amount": "97853.86",
                          "currency": {
                              "name": "руб.",
                              "code": "RUB"
                          }
                      },
                      "description": "Перевод с карты на счет",
                      "from": "Maestro 1308795367077170",
                      "to": "Счет 96527012349577388612"
                      },
                     {
                         "id": 122284694,
                         "state": "EXECUTED",
                         "date": "2019-08-08T21:58:06.688541",
                         "operationAmount": {
                             "amount": "98657.83",
                             "currency": {
                                 "name": "руб.",
                                 "code": "RUB"
                             }
                         },
                         "description": "Перевод организации",
                         "from": "Счет 99668626339273709694",
                         "to": "Счет 27219929444683698245"
                     }
                     ]
    return expected_data


def test_load_operations_json(data):
    actual_data = load_operations_json(test_json_path)
    assert actual_data == data
    assert isinstance(actual_data, list)


def test_hide_number_from():
    card_number_from = '7158300734726758'
    expected = '7158 30******6758'
    assert hide_number_from(card_number_from) == expected


def test_hide_number_to():
    input_data = '35383033474447895560'
    expected = '**5560'
    assert hide_number_to(input_data) == expected


def test_sorted_operations(data):
    assert sorted_operations(data)


def test_get_date():
    test_date = {"date": "2019-07-13T18:51:29.313309"}
    assert get_date(test_date) == '13.07.2019'
