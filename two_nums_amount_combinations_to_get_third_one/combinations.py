def search_combinations(first_num=16, second_num=18, needed=170, isGreedSearch=True, isSort=False):
    """
    :param first_num: first number for iteration
    :param second_num: second number for iteration
    :param needed: number that should be returned by sum of some amount first_nums and second_nums
    :param bool isGreedSearch: define if we take only needed number or also +/- 2 numbers
    :param bool isSort: define if we sort list 'result_array' according to third element
    :return: list of tuples 'result_array'

    Function loops over the numbers appropriately to find all combinations of the sum
    of two numbers.
    Their sum must be equal (or 1 / 2  more / less ) to the 'needed' )
    """
    answers = [i for i in range(needed - 2, needed + 3)]
    result_array = []
    some_range = answers[-1] // min(first_num, second_num) + 1
    for i in range(0, some_range):  # for first_num
        for j in range(0, some_range):  # for second_num
            temp_result = first_num * i + second_num * j
            if isGreedSearch:
                if temp_result in answers:
                    t = (i, j, temp_result)
                    result_array.append(t)
            else:
                if temp_result == needed:
                    t = (i, j, temp_result)
                    result_array.append(t)

    if isSort:
        result_array.sort(key=lambda tup: tup[2])

    for i in result_array:
        k = i[0]
        k2 = i[1]
        res = i[2]  # first_num * k + second_num * k2
        print(f"{first_num}*{k} + {second_num}*{k2} = {res}")

    return result_array


print(search_combinations(2, 4, 8, isSort=True))