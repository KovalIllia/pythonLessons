# import pytest
# from pytestLessons.tests import conftest
# # pytest --fixtures ["/home/koval_i/PycharmProjects/pythonLessons/pytestLessons/tests"]


def test_sending_mail_1(set_up):
    print("Letter is sended_1")

def test_sending_mail_2(set_up,another_module_fixture):
    print("Letter is sended_2")

def test_sending_mail_3(set_up,another_function_fixture):
    print("Letter is sended_2")

