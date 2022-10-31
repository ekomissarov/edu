class slo:

    __slots__ = "field", "schmield"
    readonly = 100500  # поскольку не объявлена слотом мы ничего не сможем ей присвоить
    # на самом деле слоты реализуются через дескрипторы

    def __init__(self, f, s):
        self.field, self.schmield = f, s


c = slo(33, 44)
print(c.field, c.schmield)
c.field, c.schmield = 77, 88
print(c.field, c.schmield)
