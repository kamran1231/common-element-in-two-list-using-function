

#define afunction which takes two list and return a list which contain common elements of both side:

#BLL
def common_list(l,l2):
    list1 = []
    for i in l:
        if i in l2:
            list1.append(i)
    return list1


#PL
l = [1,2,3,4,5,6]
l2 = [3,2,4,6,4,6,7,8]
print(common_list(l,l2))