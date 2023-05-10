import concurrent.futures
import hashlib
import time


def digest(t):
    hash = hashlib.sha256()
    time.sleep(3)
    for i in range(t*1000000):
        hash.update('hogehoge'.encode('utf-8'))
    return hash.hexdigest()


task_list = [1, 1, 1, 2, 2, 3]
executor = concurrent.futures.ProcessPoolExecutor(max_workers=4)
futures = [executor.submit(digest, t) for t in task_list]
print('start')
completed = concurrent.futures.as_completed(futures, 1)
print('end')

time.sleep(3)
# result()で待機した時からタイムアウトが1秒なので
# 4つだけ終了して残りはタイムアウトする。
for future in completed:
    print(future.result())

# result()時点で既に全て終了している
for future in futures:
    print(future.result())


executor.shutdown()
