'''
https://docs.python.org/3/tutorial/controlflow.html#function-annotations

'''

def f(ham: str, eggs: str = 'eggs') -> str:
    '''
    Строка документации. Документация к функции.
    :param ham:
    :param eggs:
    :return:
    '''

    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print(f('spam'))
print(help(f))