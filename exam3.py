'''
def subsets(set1, set2):
    for n in set1:
        if n not in set2:
            return False
        else:
            return True
set1= (4,5,6,7)
set2 = (4,5,6,7,8,9)
is_subset = subsets(set1, set2)
print(is_subset)


for num in range(0, len(numbers)):
    for i in times:
        print(i)
        minutes = i.split(':')
        if int(minutes[0]) > 0:
            total_time += int(minutes[0])*60
        total_time += int(minutes[1])
    call_dict[num] = total_time


def unique(list1):
    setlist = set(list1)
    list2 = setlist
    return setlist
list1 = [1,2,3,4,4,5,6,7,7,7,8,9]
newlst = unique(list1)
print(newlst)


def find_in_2D_list(my_2Dlist, val):
    for i in range(len(my_2Dlist)):
            # iterate through inner list, which is outer list at i
        for j in range(len(my_2Dlist[i])):
            if my_2Dlist[i][j] == val:
                    # found the value
                print("found at index " + str(i) + ", " + str(j))
                found = True
                if not found:
                    print("The value does not exist.")

my_2Dlist = [1,2,3,4,5], ['a','b','c','d'],['abc','acb']
val = 'b'
find_in_2D_list(my_2Dlist, val)

some_list = [[1, 45, 6] , [‘i’, ‘love’, ‘110’], [‘is’, ‘it’, ‘Thanksgiving’] ]
    for i in range(len(some_list)) :
        for j in range(len(some_list)) :
            print(some_list[j])
'''

def anagram(var1, var2):
    var1dict = dict((l, var1.count(l)) for l in set(var1))
    print(var1dict)

var1 = 'iceman'
var2 = 'cinma'
anag = anagram(var1, var2)
print(anag)