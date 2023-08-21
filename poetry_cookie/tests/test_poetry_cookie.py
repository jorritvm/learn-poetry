from poetry_cookie import poetry_cookie

def test_give_me():
    assert poetry_cookie.give_me(5) == 5
    assert poetry_cookie.give_me(0.0) == 0.0
    assert poetry_cookie.give_me(True) == True