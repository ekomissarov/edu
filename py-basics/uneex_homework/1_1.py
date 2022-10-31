a = eval(input("Введите объект (пустой объект - выход): "))
while(a):
    if type(a) is str:
        print ("Это строка!")
        break
    a = eval(input("Введите объект (пустой объект - выход): "))
else:
    print("Строки не было")
