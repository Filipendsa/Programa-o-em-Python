for tabuada in range(1, 11):
    print("Tabuada do %d" % tabuada)
    for count in range(10):
        print("%d x %d = %d" % (tabuada, count + 1, tabuada * (count + 1)))
    print("\n")