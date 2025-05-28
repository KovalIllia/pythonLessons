"""Задача 1: Робота з тимчасовим файлом
Мета: Навчитись створювати і знищувати файл у тесті.

📌 Умова:

Створи фікстуру temporary_file, яка:

Створює файл temp.txt з якимось вмістом ("hello world").

Через yield передає шлях до файлу.

Після виконання тесту — видаляє файл.

🧪 Тест: перевір, що файл існує і містить "hello world"."""

import pytest
import os
#
@pytest.fixture()
def temporary_file():
    new_value = "hello world"
    fw=open('doc/Les29.txt','a')
    fw.write(f"{new_value}\n")#update doc
    fw.close()#close doc
    yield 'doc/Les29.txt'
    os.remove('doc/Les29.txt')

# def writeNewValue():
#     new_value = "hello world"
#     fs = open('doc/file1.txt', 'a')  # create doc
#     fs.write(f"{new_value}\n")#update doc
#     fs.close()#close doc

def test_file_content(temporary_file):
    assert os.path.exists(temporary_file)
    fa = open(temporary_file, 'r')
    text = fa.read()
    assert "hello world" in text
    fa.close()
    print(text)


"""✅ Задача 2: Симуляція підключення до API
Мета: Попрактикуватися в імітації зовнішнього ресурсу.

📌 Умова:

Створи фікстуру api_client, яка:

Виводить "Підключення до API..." (setup).

Повертає об’єкт (наприклад, словник) через yield.

Після тесту виводить "Відключення від API..." (teardown).

🧪 Тест: перевір, що в об'єкті є ключ "status" із значенням "connected"."""


@pytest.fixture()
def api_client():
    print("Підключення до API...")
    user_data = {"status":"connected","user":"admin"}
    yield user_data
    print("Відключення від API...")

def test_newObject(api_client):
    assert api_client["status"]=="connected"
    print(api_client)



"""✅ Задача 3: Тимчасовий список користувачів
Мета: Вивчити як підготувати ресурс, який змінюється під час тесту.

📌 Умова:

Створи фікстуру user_list, яка:

Ініціалізує список з одним користувачем: ["admin"].

Повертає цей список у тест через yield.

🧪 Тест: додай користувача "test_user" до списку і перевір, що тепер у ньому два елементи."""


@pytest.fixture()
def user_list():
    new_userlist=["admin"]
    yield new_userlist

def test_addingNewUser(user_list):
    user_list.append("test_user")
    assert len(user_list)==2
    assert "test_user" in user_list
