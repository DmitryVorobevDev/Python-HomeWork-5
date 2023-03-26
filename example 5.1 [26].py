# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b.
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def result_searchig (number, degree):
    if degree == 0:
        return 1
    if degree == 1:
        return number
    return number * result_searchig(number, degree - 1)
print (result_searchig(2, 4))