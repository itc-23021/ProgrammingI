numbers = [1, 1, 2, 3, 5, 8, 3, 13, 21]
x = 0
for n in numbers:
    if n > 10:
        break
    x += n
    # 20が出力される
