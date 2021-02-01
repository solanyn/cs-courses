def chop(li):
    if len(li) > 2:
        li = li[1:len(li) - 1]

    return None

def middle(li):
    if len(li) > 2:
        return li[1:len(li) - 1]
    
    return []

li = [1, 2, 3]
print('Testing chop() and middle() functions')

print(li)

chop(li)

print('Chop: %s' % li)
print('Middle: %s' % middle(li))

