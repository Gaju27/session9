# The main topics covered are 

 *  Decorators
 *  Parameterized Decorators
 *  Assignment

## Main and test functions

   1. [session9.py](https://github.com/Gaju27/session9/blob/master/session9.py)
   2. [test_session9.py](https://github.com/Gaju27/session9/blob/master/test_session9.py)

## Decorators
    
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.  Let's understand with simple example for decorator and its test.

This is the basic Decorator function accepts input as a function and sets function variable to True and return back the function
``` 
def decorate(f):
    f.decorated = True
    return f
```
We call this decorate function with `@decorate` to another function that added with decorate functionality.


```
def test_decorate_basic_test():
    @decorate
    def mock():
        return True
    assert mock.decorated is True
```

### Odd_timer
Function has to run only for odd seconds.

 - Below program accepts function and runs only if the current times has odd seconds. 
  - if it was in even seconds it would error out.

```

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

```

### logging message

- Below program accepts function and log message for 
        - Name of the function
        - Line details
        - time it was called
    example logs information
    * `2020-09-25 17:30:51,755 :: INFO :: return_logger :: 36 :: is the line and Function called for "odd_timer_check"`

```
def logger_message(fn):
    '''Function is to log the message to get name with and line and docstring'''
    def return_logger(*args, **kwargs):
        logging.info(f'is the line and Function called for "{fn.__name__}"')
        logging.info(f'docstring summary:{fn.__doc__}')
    return return_logger

```
Simple logging function written [logger.py](https://github.com/Gaju27/session9/blob/master/logger.py)

## Authenticate
We authenticate the user for the correct password. If the user enters the wrong password it will throw an error message.
```
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
```
where `current_password()` function used to accept the value as input as below.

```
def set_password():
    password = ''

    def inner():
        """this is the inner closure
         """
        nonlocal password
        if password == '':
            password = input()
        return password

    return inner
```

## timed(n time)
```
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
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
