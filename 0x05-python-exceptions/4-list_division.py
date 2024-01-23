#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list_ = []

    for i in range(list_length):
        try:
            e1 = my_list_1[i] if i < len(my_list_1) else 0
            e2 = my_list_2[i] if i < len(my_list_2) else 0

            div_result_ = e1 / e2
        except ZeroDivisionError:
            print("division by 0")
            div_result_ = 0
        except (TypeError, ValueError):
            print("wrong type")
            div_result_ = 0
        except IndexError:
            print("out of range")
            div_result_ = 0
        finally:
            result_list_.append(div_result_)

        return result_list_
