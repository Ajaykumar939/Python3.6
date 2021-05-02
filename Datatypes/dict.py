# a Dictionary can be created by placing sequence of elements within curly {} braces,
# separated by ‘comma’. Dictionary holds a pair of values, one being the Key and
# the other corresponding pair element being its Key:value. Values
# in a dictionary can be of any datatype and can be duplicated,
# whereas keys can’t be repeated and must be immutable.


Dict = {1: 'xyz', 2: 'For', 3: 'abc'}
print(Dict)
# print(Dict.keys())
# print(Dict.values())
Dict[3] = 'pk'
Dict[4] = 'ntr'
print(Dict)
