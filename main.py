# YOUR CODE HERE
num = int(input())
list1 = []
list2 = []
update_list = []
for i in range (num) :
    a = int(input())
    list1.append(a)
for i in range (num) :
    b = int(input())
    list2.append(b)

def summation() :
    global list1, list2, update_list, n
    for i in range (num) :
        sum = 0
        sum += list1[i] + list2[i]
        update_list.append (sum)
    return update_list

def find_min_max():
    global update_list
    update_list.sort
    m_x = []
    min = update_list[0]
    max = update_list [num-1]
    m_x.append(min)
    m_x.append(max)
    return tuple(m_x)

print(summation())
print(find_min_max())





