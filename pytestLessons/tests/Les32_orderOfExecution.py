import pytest


@pytest.mark.run(order=2)
def test_method_1():
    print("Letter is sended_1")

@pytest.mark.run(order=1)
def test_method_2():
    print("Letter is sended_2")

@pytest.mark.run(order=3)
def test_method_3():
    print("Letter is sended_3")

@pytest.mark.run(order=5)
def test_method_4():
    print("Letter is sended_4")

@pytest.mark.run(order=4)
def test_method_5():
    print("Letter is sended_5")