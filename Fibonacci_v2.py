#Fibo_v2 Just necessary number of list elements

Fibo = [0, 1]

for i in range(0, 30):
    try:
        print(str(i+1) + ". " + str(Fibo[i]))
    except IndexError:
        Fibo.append(Fibo[i-2]+Fibo[i-1])
        print(str(i+1) + ". " + str(Fibo[i]))
