    """concurrent.futuresのProcessPoolExecutorのサンプル

    複数の巨大な数の素数判定を並列処理によって解く
    並行処理であるasyncioで行った例(async_prime.py)と比較すると若干速いことが分かる
    """
from concurrent import futures
import time

def is_prime(num):
    if num < 2: return False
    if num == 2: return True
    if (num % 2) == 0: return False
    i = 3
    while(num >= i*i):
        if((num % i) == 0):
            return False
        i += 2
    return True

if __name__ == "__main__":
    values = [
        112272535095293,
        112582705942171,
        112272535095293,
        115280095190773,
        115797848077099,
        1099726899285419,
    ]
    future_dict = []

    start = time.time()
    with futures.ProcessPoolExecutor(max_workers=4) as executor:
        # 扱い方はThreadPoolExecutorとほとんど同じ
        future_dict = {executor.submit(is_prime, num=val): val for val in values}
    # futures.as_completedは処理が終わった順にそのFutureオブジェクトを返していくジェネレーターになる
    completed_tasks = futures.as_completed(future_dict)
    t = time.time() - start

    for future in completed_tasks:
        # 処理の結果はFutureオブジェクトのresult()から得られる
        result = future.result()
        # future_dictがFutureオブジェクトをキーとした辞書なので
        # 処理の対象となった数は次のようにして得られる
        value = future_dict[future]
        print(f'{value} is ' + ('' if result else 'not ') + 'a prime number')
    print(f'time: {t}sec')
