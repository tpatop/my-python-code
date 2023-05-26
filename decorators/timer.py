import time
import atexit
from functools import wraps


@atexit.register
def finish():
    '''Позволяет запустить функцию после окончания отработки скрипта'''
    print("\n\tВсе процессы были завершены!\n")


def run_times(counts=1):
    '''
    Данный декоратор принимает функцию и количество повторения,
    выводит среднее время
    '''
    def _run_time(func):
        running_list = list()

        @wraps(func)
        def _wrapper(*args, **kwargs):
            if counts == 1:
                print('''
                    Выполнение функции 1 раз не позволяет объективно оценить скорость выполнения программы, \n
                    так как во многом будет зависеть от загруженности процессора и прочих факторов.\n
                    Декорируйте функцию с заданным количеством перезапусков, например: "@run_times(5)"\n'
                    ''')
            elif counts <= 0:
                print(f'Не стоит пытаться запустить проверку с отрицательным или нулевым значением перезапусков!\n'
                      f'Декорируйте функцию с заданным количеством перезапусков, например: "@run_times(5)"\n')
                return None
            '''Цикл для перезапуска программы указанное количество раз'''
            for _ in range(counts):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                running_list.append(end - start)
            print(f'Фунцкия "{func.__name__}" в среднем выполнялась {sum(running_list) / counts:.9f} сек.\n'
                  f'Количество прогонов = {counts}.\n')
            return result
        return _wrapper
    return _run_time


##################################################################################
# Для тестирования
def test():
    import random as r, string as s

    restart = 10

    @run_times(restart)
    def gen_generator_text(n:int)->str:
        st = s.printable
        yield ''.join([r.choice(st) for _ in range(n)])

    @run_times(restart)
    def gen_text(n: int)->str:
        st = s.printable
        return ''.join([r.choice(st) for _ in range(n)])

    number = 10**5 #Количество символов текста
    gen_text(number)
    gen_generator_text(number)


#print(list(gen_generator_text(number))[0]) #Вывод рандомного текста

# '''Вывод документации функции'''
# print(f'{gen_text.__name__ = }')
# print(f'{gen_text.__doc__ = }')
# print(f'{gen_text.__annotations__ = }')

# '''Вывод полученных результатов'''
# print(gen_text(100))
# print(list(gen_generator_text(100)))