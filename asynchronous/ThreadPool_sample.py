from concurrent import futures
import random
import time

def func(idx):
    sleep_sec = random.randint(1, 10)
    print(f'process: {idx}, Waiting for {sleep_sec} seconds...')
    time.sleep(sleep_sec)
    print(f'process: {idx} ended...')

if __name__ == "__main__":
    future_list = []
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        # executor.submitの第一引数に処理対象の関数を
        # それ以降の引数にはその関数に与える引数を書く
        # 第一引数で与えた関数の返り値がそのままsubmitの返り値となる
        future_list = [executor.submit(func, idx=i) for i in range(8)]
    # futures.as_completedを呼ぶことで一通りの処理を終えるまで待つ形になる
    # この引数としてsubmitで返却された処理対象のリストを指定する
    futures.as_completed(fs=future_list)
    print('completed.')