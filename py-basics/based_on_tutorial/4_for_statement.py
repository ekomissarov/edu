#https://docs.python.org/3/tutorial/controlflow.html#for-statements
'''
в питоне есть несколько типов данных, вот основные из них:
- тюпль / кортеж / константный список ()
- список [], list()
- множества и словари {} {:}
- и др.
В примере ниже используется список. 
Для цикла for объект должен быть иттерируемый https://docs.python.org/3/tutorial/classes.html#iterators
'''

words = ['cat', 'window', 'defenestrate']
print(words)
print(dir(words), '\n\n')
for w in words:
    print(w, len(w))

'''
Если нужно изменить список в цикле, то нужно использовать его верхнеуровневую копию [:] для иттерации
'''
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print('\n',words)
