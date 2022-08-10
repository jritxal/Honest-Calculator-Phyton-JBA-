lower_camel_case = input()
res = ""
underscore = "_"
for str_ in lower_camel_case:
    if str_.isupper():
        res += underscore
    res += str_.lower()
print(res)
