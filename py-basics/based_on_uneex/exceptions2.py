class Exc(Exception):
    pass


def funex(a):
    if a<-1:
        raise Exc(a)  # решили что функция плохая вот здесь
    return a*2+1

def fun(a):
    return funex(a)**(1/2)



# а решили что с этим делать здесь, в отличие от проверок if
# где принимать решение нужно будет по месту
try:
    a = fun(-9)
except Exc as E:
    print ("Invalid", E)
    a = E.args

print(a)



# протокол контекст менеджера и with
# https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions
# https://docs.python.org/3/reference/compound_stmts.html#with

'''
Some objects define standard clean-up actions to be undertaken 
when the object is no longer needed, regardless of whether or 
not the operation using the object succeeded or failed. 
Look at the following example, which tries to open a file and 
print its contents to the screen.

for line in open("myfile.txt"):
    print(line, end="")

The problem with this code is that it leaves the file open for 
an indeterminate amount of time after this part of the code 
has finished executing. This is not an issue in simple scripts,
 but can be a problem for larger applications. 
 The with statement allows objects like files to be used in a way 
 that ensures they are always cleaned up promptly and correctly.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
        
After the statement is executed, the file f is always closed, 
even if a problem was encountered while processing the lines. 
Objects which, like files, provide predefined clean-up 
actions will indicate this in their documentation.

аналог try except finaly, где в finaly будет закрытие файла

'''