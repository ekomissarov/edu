def concat1(separator, *args):
    print(separator.join(args))

def concat2(*args, sep = '/'):
    print(sep.join(args))

concat1("-","QQ","QKRQ")
concat2("QQ","QKRQ","RQ")
concat2("QQ","QKRQ","RQ", sep='#')

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print(arguments)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    print(keywords)
    for kw in keywords:
        print(kw, ":", keywords[kw])
# аналогично, но без лишней операции индексирования:
    for k, v in keywords.items():
        print(k, ":", v)

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
'''
# последовательность аргументов не гарантируется до версии Python 3.6.х
Note that the order in which the keyword arguments are printed 
is guaranteed to match the order in which 
they were provided in the function call.

-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch

'''

