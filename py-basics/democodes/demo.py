'''


'''

n = list(map(int, input().split()))
#list = [i for i in n if i%2]
print(min(filter(lambda v: v%2, n)))
#print(min(list))