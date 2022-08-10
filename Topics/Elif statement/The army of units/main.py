units = int(input())
limits = ([1, "no army"], [10, "few"], [50, "pack"], [500, "horde"], [1000, "swarm"])
for limit in limits:
    if units < limit[0]:
        print(limit[1])
        break
else:
    print("legion")
