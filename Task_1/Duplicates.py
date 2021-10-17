def missing_and_duplicates_list(list):
    
    single_nums=[]   #list for single occure 
    duplicates = []   #list for more that one occure 
    full_list = []   #list without duplicates 
    
    missing=[]   #list of missing nums
    list.sort()  #sort out ascending order 
    

    for i in list:                      # for loop for iter list 
        if i not in single_nums:        # Iterate List with each value to check num not present in single_nums lsti
            single_nums.append(i)       # whether above condition is true then i value will added in single_nums lsti or it is not true then pass towards next condition
            single_nums.sort()          # before the exit of this loop single_nums list will sort in ascending orede 
            
        elif i not in duplicates:        # Iterate List with each value to check num not present in duplicate list
            duplicates.append(i)         # whether above condition is true then i value will added in duplicate list or it is not true then pass towards next condition
            duplicates.sort()            # before the exit of this loop duplicate list will sort in ascending orede
        else:
            pass                        # when all above conditions are getting false then this condition passes towards 
    

    for k in range(single_nums[0],single_nums[-1]):   # this iteration creatted for getting full list (missing + original list), 
                                                        #  and it retreve the num of lowest num of otiginal and ends with highest num 
        full_list.append(k)                           # it appends all num lowest to highest num
        if k not in  single_nums:                     # this condition checking missing value for appending in missing list
            missing.append(k)
            missing.sort()
    print('Duplicate Num list: {}'.format(duplicates))
    print('Missing Num list: {}'.format(missing))
    print('Single Occure Num list: {}'.format(single_nums))
    print('Missing and Single Occure Num list: {}'.format(full_list))
    print('original list: {}'.format(list))


a = [5, 6, 7, 2, 8, 3, 4, 8, 12, 15, 25, 21, 15 ,6]
missing_and_duplicates_list(a)
