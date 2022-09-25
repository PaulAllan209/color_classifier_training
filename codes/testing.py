anon_func = lambda x: min(x, key=lambda i:i[-1])

test_list = ['wow1', 'wow2', 'wow3', 'wow4']
test_list1 = ['wo1', 'wo2', 'wo3', 'wo4']

print(anon_func(test_list))
print(anon_func(test_list1))
