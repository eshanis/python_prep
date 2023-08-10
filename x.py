var = 10
for i in range(10):
    for j in range(2, 10, 1):
        print('var is',var, 'j is',j,'i is',i)
        if var % 2 == 0:
            print('even number' ,var, 'i is', i,'j is',j)
            continue
            print('number is', var, 'i is', i,'j is',j)
            var += 1
    print('i am outside the for loop of j', 'i is', i, 'j is',j,'var is',var)
    var+=1
else:
    print('reached else, number is', var, 'i is', i,'j is',j)
    var+=1
print(var)