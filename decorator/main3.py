import time
from functools import wraps

cache = {}


def generate_cache_key(prefix, *args, **kwargs):
    return prefix + str(args) + str(kwargs)


def cache_function(timeout=5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            params = args[1:]
            class_name = func.__qualname__.split(".")[-2]
            cache_key = generate_cache_key(f"{class_name}.{func.__name__}", *params, **kwargs)

            # キャッシュにあるか確認
            if cache_key in cache:
                result, expire_time = cache[cache_key]
                if time.time() < expire_time:
                    print(f"✅ キャッシュヒット: {cache_key}")
                    return result
                else:
                    print(f"⚠️ キャッシュ期限切れ: {cache_key}")

            # 関数を実行してキャッシュに保存
            result = func(*args, **kwargs)
            cache[cache_key] = (result, time.time() + timeout)
            print(f"💾 キャッシュ保存: {cache_key}")
            return result
        return wrapper
    return decorator


class Calculator:
    @cache_function(timeout=5)
    def slow_add(self, x, y):
        print("計算中...")
        time.sleep(2)  # 時間がかかる処理をシミュレート
        return x + y


if __name__ == "__main__":
    calc = Calculator()

    print(calc.slow_add(2, 3))  # 初回は計算する
    print(calc.slow_add(2, 3))  # すぐはキャッシュが返る
    time.sleep(6)               # 6秒待ってキャッシュ期限切れ
    print(calc.slow_add(2, 3))  # 再度計算される
