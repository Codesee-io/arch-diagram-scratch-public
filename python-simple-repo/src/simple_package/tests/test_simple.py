from ..simple import add_one, invoke_add_two
from ..helper import add_two

def test_add_one():
    assert add_one(1) == 2

def test_invoke_add_two():
    assert invoke_add_two(1) == 3

def test_add_two():
    assert add_two(1) == 3
