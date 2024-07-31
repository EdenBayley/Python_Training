
class ListExample():

    nums = [10,20,30,40,23]
    class_names = ["Amit", "Eden", "Ran"]
    new_nums = []

    var_0 = nums[0]  #יהיה שווה 10
    var_1 = class_names[1] #יהיה שווה Eden
    # 0 זה הראשון, 1 זה השני
    length_my_list = len(nums)
    before_last_example_1 = nums [length_my_list-1] #how to get the last variable of list
    before_last_example_2 = nums [-1:]
    example = nums [-2:]
    example_2 = nums [:2]
    nums [2:]
    index = class_names.index ("Eden")
    class_names.append ("Shira")
    class_names.insert(3,"Aviv")
    class_names.remove ("Aviv")

#example how to go over all list

    for num in nums:
        new_num = num+5
        print (f'{new_num}')
        new_nums.append (new_num)

    for name in class_names:
        print (f"my name is {name}")

    print ("test end")

