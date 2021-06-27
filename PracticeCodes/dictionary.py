a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

knights = {1: 'gallahad', 2: 'robin', 3: 'brave', 4: 'kings_men'}
"""
print(knights.items())
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

for i, v in enumerate(list(knights)):
    print(i, v)
"""

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
# print(non_null)

''' 
print((1, 2, 3) < (1, 2, 4))
print([1, 2, 3] < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4) < (1, 2, 4))
print((1, 2) < (1, 2, -1))
print((1, 2, 3, 4) >= (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)) '''


def case_calc_1(cases):
    for x, y in cases:
        print(x+y)


def case_calc_2(cases):
    for x, y in cases:
        pass


case_calc_1([(1, 1), (2, 2), (3, 3)])

String1 = 'Hello'
to_list = []
for word in String1:
    to_list.append(word.upper())
print(to_list)


def case_calc(cases):
    yield [x+y for x, y in cases]


cases = [(1, 1), (2, 2), (3, 3)]
result = case_calc(cases)
print(type(result))
for i in range(len(result)):
    print(result[i])
