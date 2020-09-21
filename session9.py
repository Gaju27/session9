import datetime as d


#
# now=d.datetime.now()
# seconds=now.second
# print(type(seconds))
# if seconds%2==1:
#     print("i'm in odd zone")
# else:
#     print(" even zone")


def odd_timer(fn):
    now = d.datetime.now()
    seconds = now.second

    def inner(*args, **kwargs):
        nonlocal seconds
        if seconds % 2 == 1:
            print(f"Function{fn.__name__} called at odd second: {seconds}")
        else:
            raise Exception("Sorry! you are in the even time :) Try one more time")
        return fn(*args, **kwargs)

    return inner


def add(a, b):
    return a + b

add = odd_timer(add)

result = add(1, 2)
