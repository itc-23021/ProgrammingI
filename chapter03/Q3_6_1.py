import random

numbers = "0123456789"
sample4 = random.sample(numbers, k=4)
num4 = "".join(sample4)
while True:
    val = input()
    if val == num4:
        print("ok")
        break
else:
    print(val, ":NG")
