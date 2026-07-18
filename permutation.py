def permutations(array):
    if len(array) < 2:
        # print(array)
        # Base case, return single-element array wrapped in another array
        return [array]
    else:
        perms = []
        for index in range(len(array)):
            # Make a fresh copy of the passed array and remove the current element from it
            rest = array.copy()
            # print(array,array[index])
            rest.pop(index)
            
            # Call our function on that sub-array, storing the result: an array of arrays
            ps = permutations(rest)

            # Add the current element to the beginning of each sub-array and add the new
            # permutation to the output array
            current = [array[index]]
            for p in ps:

                perms.append(current + p)
                # print("cur",current)
                # print("P",p)
                # print("cur_P",current+p)
                
        return perms
print(permutations([1,2,3]))