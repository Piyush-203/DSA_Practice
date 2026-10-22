 

def agressive_cows(positions =[10, 1, 2, 7, 5], num_cows = 3):
    ''' Arrange the cows in such a way that the minimum distance between the 2 cows 
        should be maximum.'''
        
    n = len(positions)
    positions = sorted(positions)
    st = 0
    end = positions[n-1]
    ans = -1
    while st <= end:
        mid = st + (end - st)//2
        if is_valid_position(positions,num_cows,mid):
            ans = mid
            st = mid + 1
        else:
            end = mid - 1
    return ans
    
def is_valid_position(positions, num_cows, min_dist):
    cur_cow = positions[0]
    n = len(positions)
    num_cow_placed = 1
    for i in range(1, n):
        if positions[i] - cur_cow >= min_dist:
            cur_cow = positions[i]
            num_cow_placed+=1
        
    return num_cow_placed >= num_cows
    
print(agressive_cows())