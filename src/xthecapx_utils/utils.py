def find_pair_of_numbers(numbers, sum):
    """ Add two arguments
    Arguments:
        numbers: list of integer
        sum: the total sum of integers to search
    Returns:
        A list of pairs of integers from a list that sums to a given value
    """
    differences = {}
    pairs = []

    if not numbers or not sum:
        return []

    for number in numbers:
        cast_number = int(number)

        if (cast_number in differences):
            pairs.append((number, differences[number]))
            continue
        
        difference = sum - number
        differences[difference] = number

    return pairs

