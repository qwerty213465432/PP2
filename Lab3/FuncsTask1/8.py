def spygm(nums):
    
    has_0 = False
    has_0_0 = False

    
    for num in nums:
        
        if num == 0:
            
            if has_0:
                has_0_0 = True
        
        elif num == 7:
           
            if has_0 and has_0_0:
                return True
        
        else:
            has_0 = True

    return False


print(spygm([1,2,4,0,0,7,5]))  # True
print(spygm([1,0,2,4,0,5,7]))    # True
print(spygm([1,7,2,0,4,5,0]))    # False
