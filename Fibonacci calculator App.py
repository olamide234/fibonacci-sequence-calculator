print('Welcome to Fibonacci Calculator App')
num=int(input('how many digits of fibonacci Sequence would you like to compute? '))

fib=[1, 1]
for i in range(num-2):
    new_fib= fib[i]+ fib[i+1]
    fib.append(new_fib)

print('\nThe first ' + str(num) + ' numbers of the fibonacci sequence are: ')
for number in fib:
    print(number)

golden=[]
for i in range(num-1):
    ratio=fib[i+1]/fib[i]
    golden.append(ratio)

print('The corresponding golden ratios are: ')
for ratio in golden:
    print(ratio)