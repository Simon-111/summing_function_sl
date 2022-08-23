# summer() is a function that finds consectutive runs in a list of numbers that total a certain amount
#     eg. summer([1, 2, 3, 4, 5, 6, 7, 8], 12 would return perhaps a tuple (2, 5) which means that the slice
#    [2:5] in that list that totals 12 or returns the slice of the list that totals twelve [3, 4, 5], returns
#    None if no run of 12 is found

# Function takes in a string and a sum to be looked for
#    If the sum to be locked for is not entered a default of ten will be used
# step 1a - check if list_in is a list
# step 1b - check if all items in list in are integers
# step 1c - check if sum to be looked for is an integer
# step 1d - created  an empty list to hold tuples with the starting and ending
#           nums for a slice that equals the sum being looked for
# step 2  - for each item in the list, set running total to the value of the item
#     step 3 - check if running total equals the sum looked for
#              if it does create a tuple with the starting and ending nums for the slice that contains the total
#              and append it to the list created in step 1d and then go back to step 2 for the next item
#     step 4 - check if running total exceeds the sum looked for
#               if it does go back to step two for the next item in the list
#     step 5 - if the sum looked for does not equal or exceed the sum looked for
#              add the next element to the starting element
# step 6 - if the sum wasn't found in the list set the list created in step 1d to 'None'
# step 7 - return the list with 'None' or the tuples withe the start and stop indexes for the sums


def summer(list_nums, sum_looking_for=10):
    """This function takes a list of integers and a integer as inputs
    The function looks through the list for consecutive items that add up to the second input

    It returns a list of tuples with the start and stop indices for the slices that make up the sum
    """
    if type(list_nums) != list:  # step 1a - is the first argument a list
        raise TypeError('Expected a list for the first argument')
    else:
        for item in list_nums:  # step 1b - are all the objects in the list ints
            if type(item) != int:
                raise TypeError('All elements of the list must be integers')
    try:  # step 1c - is the second input an int
        sum_looking_for == int(sum_looking_for)
    except ValueError:
        print('Sum being looked for must be an integer')

    slices_of_sums = []  # step 1d - empty list to hold tuples of indices of slices that add up to sum_looking_for

    for index in range(0, len(list_nums)):  # step 2
        running_total = 0  # set running total to 0
        end_slice = index  # initialize the ending index to the current index
        while end_slice != len(list_nums):
            running_total += list_nums[end_slice]
            end_slice += 1  # add one ot the ending index to track the ending index
            if running_total == sum_looking_for:  # step 3
                slices_of_sums.append((index, end_slice))
                break  # break out of while loop and return to for loop
            elif running_total > sum_looking_for:  # step 4 - no matching sum for starting index
                break

    if not slices_of_sums:  # step 6
        slices_of_sums = None

    return slices_of_sums
