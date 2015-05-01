import copy as cp

def break_rings(rings):
    
    rings = list(rings)
    N = len(rings)
  
    temp = []
    
    for i in rings:
        temp.append(list(i))
    rings = temp
    
    maxi = rings[0][0]
    
    for j in rings:
        for k in j:
            if k > maxi:
                maxi = k
                
    count = [0]*maxi
 
    def add_1():
        if count[maxi-1] == 0:
            count[maxi-1] = 1
        else:
            for i in range (maxi-1,-1,-1):
                if count[i] == 1:
                    count[i] = 0
                else:
                    count[i] = 1
                    break
                
    free_rings_list = []        
    breaked_list = []

    for z in range (2**maxi-2):
        
        breaked = 0
        free_rings = 0
        
        add_1()
        
        _rings_ = cp.deepcopy(rings)
  
        for j in range (maxi):
            if count[j] == 1:
                breaked += 1
                
                for ring in _rings_:
                    try:
                        ring.remove(j+1)
                    except:
                        pass
        
        temp=[]
        
        for ring in _rings_[:]:
            if len(ring) == 1:
                temp.append(ring[0])
                _rings_.remove(ring)
        temp = set(temp)
        for ring in temp:
            _rings_.append([ring])
        
        for i in range(len(_rings_)):
            # Check if ring is free
            if len(_rings_[i]) == 1:
                temp = []
                for j in range (len(_rings_)):
                    if j != i and (len(_rings_[j])) == 2:
                        temp.append(_rings_[j])
                counter = True        
                for ring in temp:
                    if _rings_[i][0] in ring:
                        counter = False
                if counter:
                    free_rings += 1
                    
        if z != 0 and free_rings > max(free_rings_list): 
            returned = breaked
            free_rings_list.append(free_rings)
        elif z == 0:
            free_rings_list.append(free_rings)
        
    
    return returned

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
