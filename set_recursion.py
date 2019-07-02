def set_addition(num_list, size,amount):

    if amount == 0 :
        return True
    elif amount < 0:
        return False

    return set_addition(num_list, size - 1, amount) || set_addition(num_list, size - 1 , amount - num_list[size-1])


