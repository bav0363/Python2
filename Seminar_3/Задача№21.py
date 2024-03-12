#
#
# list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
#         {" V ":"S009"}, {" VIII":"S007"}]
# # new_list = []
# # for i in list:
# #      for item in i.values():
# #         new_list.append(item)
# # print(set(new_list))
#
# new_set = set()
# for i in list:
#      for item in i.values():
#         new_set.add(item)
# print(new_set)

dict_ = {"10": 0, "20": 2, "50": 7, "100": 2, "200": 0, "500": 0, "1000": 1}
dict_ = {int(key): value for key, value in dict_.items()}
print(dict_)
