input_ = input()
cafes = []
cats = []
while input_ != "MEOW":
    both = input_.split(" ")
    cats.append(int(both.pop()))
    cafes.append(both.pop())
    input_ = input()
max_ = max(cats)
print(cafes.pop(cats.index(max_)))
