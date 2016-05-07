#Adam Horvath -

Fibo = [0, 1]

for i in range(1, 30):
    Fibo.append(Fibo[i-1]+Fibo[i])

for i in range(0,30):
    print(str(i+1) + ". " + str(Fibo[i]))
