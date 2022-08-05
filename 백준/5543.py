high_burger = int(input())
middle_burger = int(input())
low_burger = int(input())
coke = int(input())
cider = int(input())

burger = [high_burger, middle_burger, low_burger]
drink = [coke, cider]

mini = 99999999
for i in burger:
    for j in drink:
        if i + j < mini:
            mini = i + j
print(mini - 50)
