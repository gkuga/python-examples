from functools import wraps


def show_func_name(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, 'を実行します')
        return func(*args, **kwargs)
    return wrapper


def show_func_name_v2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__, 'を実行します')
        return func(*args, **kwargs)
    return wrapper


@show_func_name
def main(arg):
    print(f'hello {arg}')


@show_func_name
@show_func_name
def main_call_twice(arg):
    print(f'hello {arg}')


@show_func_name_v2
@show_func_name_v2
def main_v2(arg):
    print(f'hello {arg}')


print('--- main v1 ---')
main('main')
print('--- main v1 (call twice) ---')
main_call_twice('main_call_twice')
print('--- main v2 ---')
main_v2('main_v2')
