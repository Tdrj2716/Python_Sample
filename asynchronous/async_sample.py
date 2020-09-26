"""asyncioによる並行処理の例
"""
import asyncio
import random
import time

async def func(idx):
    val = 10 - idx
    sleep_sec = (val if val > 0 else random.randint(1, 10))
    print(f'process: {idx}, Waiting for {sleep_sec} seconds...')
    await asyncio.sleep(sleep_sec)
    print(f'process: {idx} ended...')

if __name__ == "__main__":
    # イベントループを取得する
    loop = asyncio.get_event_loop()
    t = time.time()
    # asyncio.gather(*[(coroutine)])という形で複数のcoroutineを並行処理出来る
    # これはFutureオブジェクトにあたる
    gather = asyncio.gather(*[func(i) for i in range(8)])
    # run_until_complete()に並行処理(Futureオブジェクト)を渡す
    loop.run_until_complete(gather)
    t = time.time() - t
    print(f'time: {t}sec')