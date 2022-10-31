class C:
    def __getitem__(self, item):
        print(item)
        if type(item) is int:
            return item%2
        elif type(item) is slice:
            return tuple(i%3 for i in range(item.start, item.stop))
        else:
            return item

# __setitem__ аналогично присваивает какие-то значения
# __delitem__ удаляет соответствующее значение
# __missing__ что делать в случае если getitem возвращает IndexError

c = C()
print(c[123], c[1:10], c[1,2,3], c[...], sep = " - ")
# по хорошему так конечно делать не надо, потому что все-таки [] нужны для последовательности
# используя [] наверное мы все-таки хотим съэмитировать последовательность
# но в действительности все это исключителььно договоренность между программистами вами и Гвидо

