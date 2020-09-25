import inspect
import os

import Credential
import session9

README_CONTENT_CHECK_FOR = [
    'add',
    'mul',
    'div',
    'odd_timer'
    'sub',
    'logger_message',
    'set_password',
    'authenticate',
    'timed',
    'decorate',
    'calc_fib_recurse'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 1, "Make your README.md file interesting! Add atleast 500 words"


# def test_readme_proper_description():
#     READMELOOKSGOOD = True
#     f = open("README.md", "r")
#     content = f.read()
#     f.close()
#     for c in README_CONTENT_CHECK_FOR:
#         if c not in content:
#             READMELOOKSGOOD = False
#             pass
#     assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 5



def test_decorate_basic_test():
    @session9.decorate
    def mock():
        return True

    assert mock.decorated is True


def test_add_function():
    result = session9.add(1, 2)

    assert result == 3, 'Check for addition returning exact result'


def test_mul_function():
    @session9.odd_timer
    def mul(a, b):
        return a * b

    result = mul(1, 2)

    assert result == 2, 'Check for multiplication returning exact result'


def test_div_function():
    @session9.odd_timer
    def div(a, b):
        return a / session9.zero_confirm(b)

    result = div(2, 2)

    assert result == 1, 'Check for division returning exact result'


def test_sub_function():
    @session9.odd_timer
    def sub(a, b):
        return a - b

    result = sub(2, 2)

    assert result == 0, 'Check for substraction returning exact result'

def test_credential():
    add = session9.authenticate(session9.add, Credential.password)
    result = add(1, 2)

    assert result == 3, 'Check for authentication'

def test_timed_function():
    def fib(n):
        return session9.calc_fib_recurse(n)
    fib = session9.timed(fib, 10)
    result=fib(28)

    assert result==317811,'Check for fib function call'

def test_for_function_names_doc_string():
    assert session9.odd_timer.__name__=='odd_timer' ''
    assert session9.odd_timer.__doc__==' This program runs only\n' '        if seconds are odd number and return inner function\n' '        else raise error if seconds are even\n' '    '
    assert session9.logger_message.__name__=='logger_message'
    assert session9.logger_message.__doc__=='Function is to log the message to get name with and line and docstring'

def test_timed_function(capsys):
    result = session9.fib(12)
    value = capsys.readouterr()
    assert "Avg Run time:" in value.out
