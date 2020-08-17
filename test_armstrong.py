from code.armstrong import armstrong
def test_armstrong():
    assert armstrong(407)


def test_not_armstrong():
    assert armstrong(47) is False


from code.sub_dict.add_sub import *
def add_test():
    assert add(10,20) == 30

def sub_test():
    assert sub(100,20) == 80
