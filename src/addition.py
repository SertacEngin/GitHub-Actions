# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(2, -1) == 1
    assert add(3, -1) == 2
    assert add(3, -2) == 1
    assert add(3, -3) == 0
