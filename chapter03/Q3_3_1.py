my_list = ["tokyo", "oosaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
answer = []
for s in my_list:
    if len(s) >= 6:
        answer.append(s)
    print(answer)
