# Find the common keys in both of the dictionaries

def common_keys(dict1, dict2):
	lst = []
	for key in dict1.keys():
		if key in dict2.keys():
			lst.append(key)
	return lst
			

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)