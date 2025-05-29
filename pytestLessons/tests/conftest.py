import pytest


@pytest.fixture()
def set_up():
    print("User has login the system")
    yield
    print("User has left the system")


@pytest.fixture(scope="module")
def another_module_fixture():
    print("Begining")
    yield
    print("The end")

@pytest.fixture(scope="function")
def another_function_fixture():
    print("!!Begining!!")
    yield
    print("!!The end!!")