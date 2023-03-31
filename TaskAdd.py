# Чтобы лучше разобраться в типах параметров функций Инна создала inspect_function(), 
# которая в качестве аргумента принимает другую функцию (главное, не встроенную, built-in). 
# В результате работы она выводит следующие данные: название анализируемой функции, 
# наименование всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.). 
# Попробуйте повторить результат девушки.

import inspect


def my_func(a, b, c, d, *args):
	pass

def inspect_function(function1):
    print(function1.__name__)
    print(inspect.signature(function1))
    print(inspect.signature(function1).parameters.items())
    
    
    
    

inspect_function(my_func)
