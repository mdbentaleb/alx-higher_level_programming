#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for j in range(list_length):
        res = 0
        try:
            res = my_list_1[j] / my_list_2[j]
        except (ZeroDivisionError):
            print('division by 0')
        except (TypeError):
            print('wrong type')
        except (IndexError):
            print('out of range')
        finally:
            n_list.append(res)
    return (n_list)
