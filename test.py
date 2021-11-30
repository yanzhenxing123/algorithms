import time
import threading


def sleep_5_seconds():
    time.sleep(5)
    print('睡眠5秒结束')


def sleep_3_seconds():
    time.sleep(3)
    print('睡眠3秒结束')


def sleep_8_seconds():
    time.sleep(8)
    print('睡眠8秒结束')


start = time.time()
print(start)
thread_1 = threading.Thread(target=sleep_8_seconds)
thread_2 = threading.Thread(target=sleep_3_seconds)
thread_3 = threading.Thread(target=sleep_5_seconds)

thread_1.setDaemon(True)
thread_2.setDaemon(True)
thread_3.setDaemon(True)

thread_1.start()
thread_2.start()
thread_3.start()

# 主线程进入阻塞 等待thread3运行完全
thread_2.join()
end = time.time()

print("消耗时间", end - start)
