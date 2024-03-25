from libdas import add_one, division, is_palindrom
import pytest
def test_answer():
    assert add_one(5) == 5
    # assert add_one() == 5, 'Тест не прошел проверку'
'оператор assert - это встроенный оператор в python позволяющий отслеживать код, этот оператор принимает условие и необезательное сообщение которое выходит при исключении AssertionError. Исключение AssertionError выходит когда assert встречает false если assert встретит True, то ничего не произойдет'

def test_division():
    assert division(10, 5) == 2, 'Удаление неправильно работает'

@pytest.mark.parametrize(
    'a,b,res',[(10,5,2),(12,6,2,),(9,3,3)]
)
def test_division2(a,b,res):
    assert division(a,b) == res

