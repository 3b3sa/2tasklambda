numbers = [3, 12, 7, 20, 15, 2, 30, 9]

even_nums = list(filter(lambda x: x % 2 == 0, numbers))
nums_plus10 = list(filter(lambda y: y < 10,  numbers))
nums_devisible3_5 = list(filter(lambda k: k % 3 == 0 and k % 5 == 0, numbers))

print(even_nums)
print(nums_plus10)
print(nums_devisible3_5)