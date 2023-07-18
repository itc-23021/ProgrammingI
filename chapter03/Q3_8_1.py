import pickle

with open('test1.pki', 'wb')as f:
    mylist = list(range(1, 11))
    pickle.dump(, f)
    # my_listが入る
