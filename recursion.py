

def count(start, finish):
    print("begin")
    if not start > finish:
        print("middle")
        start += 1
        count(start, finish)

    print(start)
count(0,10)

1234567891011