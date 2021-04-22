import math

numbers = [-3, -5, 1, 4]
f1 = lambda x: x[0]
print('Lambda to get first item in list')
print(f'result: {f1(numbers)}')

f2 = lambda x: x ** 2/(x ** 2 + 1)
f3 = lambda x: round(x, 4)
result = list(map(f2, numbers))
final_result = list(map(f3,result))
print('Lambda on logistic function')
print(result)
print('Lambda on logistic function with round numbers to 4 decimal place')
print(final_result)