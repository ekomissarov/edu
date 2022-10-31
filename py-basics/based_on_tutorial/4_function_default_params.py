#https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        '''
        оператор in проверяет членство элемента слева, во множестве справа
        not in - отсутствие во множестве
        is / is not - проверка объектов на идентичность (id() - идунтификатор объекта)
        методы из класса:
            __contains__
            __iter__
            __getitem__
        '''
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
        
ask_ok("y/n? ")
