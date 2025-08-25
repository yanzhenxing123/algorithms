

a = 100


def func():
    global a
    a += 1000

func()
print(a)