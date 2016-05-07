#Adam Horvath -

Fibo = [0, 1]

for i in range(0, 28):
    Fibo.append(Fibo[i]+Fibo[i+1])

for i in range(0,30):
    print(str(i+1) + ". " + str(Fibo[i]))
print(Fibo)
