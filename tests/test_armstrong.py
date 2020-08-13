from code.code import armstrong


def test_armstrong():
    assert armstrong(407)


def test_not_armstrong():
    assert armstrong(47) is False
