right_combination = (2,3,5)

for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            if (c1,c2,c3) == right_combination:
                print('Found The Combination :{}'.format((c1,c2,c3)))
