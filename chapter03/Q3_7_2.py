with open("number.txt", "r") as f:
    sum = 0
    for data in f:
        num = int(data)
        sum += num
        print(sum)
        # 1から10全て足した答えが出力されるので55が出力される
