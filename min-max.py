def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        list_to_sort = args[0]    
    else:
        list_to_sort = args
    return min_sub(list_to_sort,key)   

 
def min_sub(list_to_sort, key):
    if str(type(list_to_sort)) == "<type 'generator'>":
        res = iterlen(list_to_sort)
        N = res[1]
        list_to_sort = res[0]
    else:
        N = len(list_to_sort)
        list_to_sort = list(list_to_sort)
    if key:
        min_value = key(list_to_sort[0])
        copy = list(list_to_sort[:])
        for i in range(N):
            copy[i] = key(copy[i])
            if copy[i] < min_value:
                min_value = copy[i]
        return list_to_sort[copy.index(min_value)]        
    else:
        min_value = list_to_sort[0]
        for i in range(1,N):
            if list_to_sort[i] < min_value:
                min_value = list_to_sort[i]
    return min_value


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        list_to_sort = args[0]
    else:
        list_to_sort = args
    return max_sub(list_to_sort,key)


def max_sub(list_to_sort, key):
    if str(type(list_to_sort)) == "<type 'generator'>":
        res = iterlen(list_to_sort)
        N = res[1]
        list_to_sort = res[0]
    else:
        N = len(list_to_sort)
        # it can be set
        list_to_sort = list(list_to_sort)   
    if key:
        max_value = key(list_to_sort[0])
        copy = list(list_to_sort[:])
        for i in range(N):
            copy[i] = key(copy[i])
            if copy[i] > max_value:
                max_value = copy[i]
        return list_to_sort[copy.index(max_value)]        
    else:
        max_value = list_to_sort[0]
        for i in range(1,N):
            if list_to_sort[i] > max_value:
                max_value = list_to_sort[i]
    return max_value
# making list from generator and getting it's length
def iterlen(x):
  n = 0
  list_to_sort=[]
  try:
    while True:
        list_to_sort.append(next(x))
        n += 1
  except StopIteration: pass
  return (list_to_sort,n)

min({1, 2, 3, 4, -10})
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
