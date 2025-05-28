import pytest


@pytest.fixture()
def set_up():
    print("User has login the system")
    yield
    print("User has left the system")

def test_sending_mail_1(set_up):
    print("Letter is sended")

def test_sending_mail_2(set_up):
    print("Letter is sended")

# test_sending_mail()