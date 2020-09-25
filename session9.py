import datetime as d
import logging



import Credential

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
:: %(message)s', level=logging.INFO)


def odd_timer(fn):
    ''' This program runs only
        if seconds are odd number and return inner function
        else raise error if seconds are even
    '''
    now = d.datetime.now()
    seconds = now.second

    def odd_timer_check(*args, **kwargs):
        '''this program run only if the seconds are odd else will throw an error message'''
        nonlocal seconds
        if seconds % 2 == 1:
            print(f"Function {fn.__name__} called at odd second: {seconds}")
        else:
            raise Exception("Sorry! you are in the even time :) Try one more time")
        return fn(*args, **kwargs)

    return odd_timer_check


# message={'debug':'debug','info':'info','warning':'warning'}
def logger_message(fn):
    '''Function is to log the message to get name with and line and docstring'''
    def return_logger(*args, **kwargs):
        logging.info(f'is the line and Function called for "{fn.__name__}"')
        logging.info(f'docstring summary:{fn.__doc__}')
        # logging.debug(f'is the line and Function called for "{fn.__name__}"')
        # logging.warning(f'is the line and Function called for "{fn.__name__}"')
        # logging.error(f'is the line and Function called for "{fn.__name__}"')
        # logging.critical(f'is the line and Function called for "{fn.__name__}"')
        # logging.exception('Please check value entered: ', exc_info=ValueError)
        return fn(*args, **kwargs)

    return return_logger


def set_password():
    password = ''

    def inner():
        """this is the inner closure
         """
        nonlocal password
        if password == '':
            password = 'Secret'
        return password

    return inner


def authenticate(fn, user_password):
    cnt = 0
    if user_password == current_password():
        def inner(*args, **kwargs):
            nonlocal cnt
            cnt += 1
            print(f'{fn.__name__} athenticated for {cnt} times')
            return fn(*args, **kwargs)

        return inner
    else:
        print('You scamster!!')


def timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0

        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (end - start)
        avg_run_time = total_elapsed / reps
        print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
        return result

    return inner


def decorate(f):
    f.decorated = True
    return f


current_password = set_password()
current_password()


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n - 2) + calc_fib_recurse(n - 1)


def fib(n):
    return calc_fib_recurse(n)


@logger_message
@odd_timer
def add(a, b):
    '''Function to add two variable'''
    return a + b

@logger_message
@odd_timer
def mul(a, b):
    '''Function to multiply two variable'''
    return a * b

def zero_confirm(val):
    if val <=0:
        raise ValueError ('Sorry!! Increment your value')
    return val


@logger_message
@odd_timer
def div(a, b):
    '''Function to division two variable'''
    return a / zero_confirm(b)

@logger_message
@odd_timer
def sub(a, b):
    '''Function to substract two variable'''
    return zero_confirm(a) - b

fib = timed(fib, 20)

#
add = authenticate(add, Credential.password)
mul = authenticate(mul, Credential.password)
# # add = odd_timer(add)

# result = div(1, 1)
# result_mul=mul(2,2)
# result_mul1=mul(2,2)
#
# print(result)
# # print(result_mul)

# print(fib(12))

# print(odd_timer.__doc__)
# print(odd_timer.__annotations__)
# print(odd_timer.__module__)
# print(odd_timer.__closure__)


