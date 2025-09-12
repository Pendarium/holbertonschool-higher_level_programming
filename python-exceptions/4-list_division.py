#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            element_1 = my_list_1[i]       # Peut lever IndexError
            element_2 = my_list_2[i]       # Peut lever IndexError

            if not isinstance(element_1, (int, float)) or not isinstance(element_2, (int, float)):
                print("wrong type")
                result.append(0)
            else:
                division = element_1 / element_2  # Peut lever ZeroDivisionError
                result.append(division)
        except IndexError:
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        finally:
            pass
    return result
