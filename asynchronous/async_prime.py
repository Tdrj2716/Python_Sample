    """asyncioによるCPUバウンドな処理の例
    """
import asyncio
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

# async def ~という形でpythonのnative coroutineを定義
async def calc(value):
    loop = asyncio.get_event_loop()
    # await (coroutine)の形で待ち時間の発生を明示的に示す
    # run_in_executor()を呼び出すことでnative coroutineとして処理される
    result = await loop.run_in_executor(None, is_prime, value)
    return value, result

if __name__ == "__main__":
    values = [
        112272535095293,
        112582705942171,
        112272535095293,
        115280095190773,
        115797848077099,
        1099726899285419,
    ]
    # イベントループを取得する
    loop = asyncio.get_event_loop()
    start = time.time()
    # asyncio.gather(*[(coroutine)])という形で複数のcoroutineを並行処理出来る
    # これはFutureオブジェクトにあたる
    gather = asyncio.gather(*[calc(val) for val in values])
    # run_until_complete()に並行処理(Futureオブジェクト)を渡す
    loop.run_until_complete(gather)
    t = time.time() - start

    # Futureオブジェクトのresult()から処理結果を得ることが出来る
    print(gather.result())
    # 今回はgatherで複数の処理が並行でなされているため, それらの結果がリストとして得られる
    print(f'time: {t}sec')
