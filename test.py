s1 = input()
s2 = input()

for c in s1:
    if c not in s2:
        print(c, end='')