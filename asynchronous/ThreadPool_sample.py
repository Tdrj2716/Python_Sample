"""concurrent.futuresのThreadPoolExecutorのサンプル

    待ち時間の発生する処理を並行で行う例
    並行で行わない場合やasyncioで行った例(async_sample.py)と比較する
"""
from concurrent import futures
import random
import time

def func(idx):
    val = 10 - idx
    sleep_sec = (val if val > 0 else random.randint(1, 10))
    print(f'process: {idx}, Waiting for {sleep_sec} seconds...')
    time.sleep(sleep_sec)
    print(f'process: {idx} ended...')

if __name__ == "__main__":
    future_list = []
    t = time.time()
    with futures.ThreadPoolExecutor() as executor:
        # executor.submitの第一引数に処理対象の関数を
        # それ以降の引数にはその関数に与える引数を書く
        # 第一引数で与えた関数の非同期実行を管理しその結果を保持するFutureオブジェクトがそのままsubmitの返り値となる
        future_list = [executor.submit(func, idx=i) for i in range(8)]
    # futures.as_completedを呼ぶことで一通りの処理を終えるまで待つ形になる
    # この引数としてsubmitで返却された処理対象のリストを指定する
    futures.as_completed(fs=future_list)
    t = time.time() - t
    print(f'time: {t}sec')

    t = time.time()
    for i in range(8): func(i)
    t = time.time() - t
    print(f'time: {t}sec')