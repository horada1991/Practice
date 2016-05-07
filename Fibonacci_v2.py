#Fibo_v2 Just necessary number of list elements

Fibo = [0, 1]

num = int(input("How many Fibonacci number should I print out? "))
for i in range(0, num):
    try:
        print(str(i+1) + ".\t" + str(Fibo[i]).rjust(80))
    except IndexError:
        Fibo.append(Fibo[i-2]+Fibo[i-1])
        print(str(i+1) + ".\t" + str(Fibo[i]).rjust(80))
