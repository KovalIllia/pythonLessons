"""Задача 1: Ініціалізація БД на рівні модуля
📌 Умова:

Створи фікстуру db_connection з scope="module", яка:

виводить Підключення до БД на початку,

повертає фіктивне з’єднання (наприклад, словник),

після тестів — виводить Відключення від БД.

🧪 Напиши два тести, які використовують цю фікстуру, і перевір, що повідомлення про підключення з'являється лише один раз."""
from contextlib import nullcontext

import pytest

@pytest.fixture(scope="module")
def db_connection():
    print("Підключення до БД...")
    dict_connection = {"connection_to_bd":True}
    yield dict_connection
    print("Відключення від БД...")

def test_firstConnection(db_connection):
    print(f"ID об'єкта db_connection: {id(db_connection)}")
    db_connection["user"] = "admin"
    assert db_connection["user"] == "admin"

def test_secondConnection(db_connection):
    print(f"ID об'єкта db_connection: {id(db_connection)}")
    assert db_connection["user"] == "admin"



"""✅ Задача 2: Тимчасові об'єкти з коротким життям
📌 Умова:

Створи фікстуру create_temp_user з scope="function", яка:

виводить Створення користувача на початку,

повертає ім’я користувача,

після тесту — виводить Видалення користувача.

🧪 Створи 3 тести, які викликають цю фікстуру. Перевір, що створення і видалення користувача виконується окремо для кожного тесту."""

@pytest.fixture(scope="function")
def create_temp_user():
    print(f"creating new user!")
    user_name = "test_user"
    print(user_name)
    yield user_name
    print(f"deleting created user!")
    print(user_name)

def test_checking_1(create_temp_user):
    assert create_temp_user != None
    print(id(create_temp_user))
    print(create_temp_user)

def test_checking_2(create_temp_user):
    assert create_temp_user != None
    print(id(create_temp_user))
    print(create_temp_user)

def test_checking_3(create_temp_user):
    assert create_temp_user != None
    print(id(create_temp_user))
    print(create_temp_user)







"""✅ Задача 3: Комбіноване використання scope="module" та scope="function"
📌 Умова:

Створи:

фікстуру server зі scope="module" — імітує запуск сервера,

фікстуру session зі scope="function" — імітує початок сесії користувача.

🧪 Напиши 2 тести, які використовують обидві фікстури, і переконайся, що:

Сервер запускається один раз,

Сесія створюється щоразу наново."""

@pytest.fixture(scope="module")
def server():
    print("Starting the server")
    create_connection={"connection":"success"}
    yield create_connection
    print("Closed the server")

@pytest.fixture(scope="function")
def session():
    print("Starting the session")
    create_session = {"session": "created"}
    yield create_session
    print("Closed the session")

def test_firstChecking(server,session):
    print(id(session))
    assert server["connection"]=="success"
    # assert session!=None

def test_secondChecking(server,session):
    print(id(session))
    assert session["session"]=="created"
    # assert server!=None