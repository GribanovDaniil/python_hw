# Напишите декоратор печатающий время выполения данной функции

import time

def decorete(func):
    def log():
        start = time.time()
        func()
        end = time.time()
        all = end - start
        print(all)
    return log

@decorete
def func_to_decor():
    for i in range(1000):
        print(i)
func_to_decor()