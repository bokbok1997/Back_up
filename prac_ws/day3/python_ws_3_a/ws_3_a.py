def my_multi(number_1, number_2):
    return number_1 * number_2
result_1=my_multi(2,3)


def is_negative(number):
    if number <= 0 :
        return True
    else:
        return False
result_2 = is_negative(3)

def default_arg_func(default='기본값'):
    return default

result_3 = default_arg_func()
result_4 = default_arg_func('다른 값')


print(result_1)
print(result_2)
print(result_3)
print(result_4)