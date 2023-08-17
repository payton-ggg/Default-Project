num = input()
sum_even_pos = 0
i = 0
while i < len(num):
    if i % 2 == 0:
        sum_even_pos += int(num[i])
    i += 1
print(sum_even_pos)
