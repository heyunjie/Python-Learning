# print
print('Hello World')
print('Hello'+'World!')
x = 1
print(x)

type() # class()
int() # as.int()
'This is a string'[1] #字符串视为字符列表

nam = input('Who are you?')
print('Welcome',nam)

# Demo---convert elevator floor
inp = input('European floor number?')
usf = int(inp) + 1
print('USA floor number is',usf)

# conditional statement: if()   # indentation replaces {}
y = 5
if y <10:
    print('y is samller than 10')
    print('....')
    print('....')
else:
    print('y is greater than or equal to 10')
# more about conditional statement if elif() else(); only one can be executed
if y<3:
    print('small')
elif y<6:
    print('medium')
else:
    print('large')

# try and except 处理异常
a=10
b=0
try:
    c = a/ b
    print(c)
except (ZeroDivisionError):
    print('error')
else:
    print('no error')
print('done')

# try, except and finally 处理异常
a = 10
b = 0
try:
    c = a/b
    print(c)
except (ZeroDivisionError):
    print('ZeroDivisionError happens')
except (AssertionError):
    print('AssertionError happens')
else:
    print('No error')
finally:
    print('all done')


# functions
def Hello_world(x):
    print('Hello World'+ x) # or return 'Hello World' + x

Hello_world('!')

# 格式替换
print('%s can be %s' % ('string','interpolated'))
print('{0} can be {1}'.format('string','interpolated'))
print('{name} wants to eat {food}'.format(name='Bob',food='burger'))

# while loops
a = 5
while a<10:
    print('a is still less than 10;'+' a is equal to %d'%(a))
    a = a + 1
# infinite loop starts with True
while True:
    line = input('>')
    print(line)
print('All done')

# continue & break
while True:
    line = input('>')
    if line == '#':
        continue     ## return to while again向上
    if line == 'done':
        break        ## escape the loop block向下
    print(line)
print('All done')

# for loops
for i in [5,4,3,2,1]:
    print(i)
print('All done!')

friends  = ['Joseph','Spring','Sarah']
for friend in friends:
    print('Happy New Year: ',friend)

# Example: How to identify the largest number?
largest_so_far = -1
Num = [12,23,56,21,45]
for num in Num:
    if num > largest_so_far:
        largest_so_far = num
print('the largest number is %d'%largest_so_far)

# Example: find the sequence of a set of number:
Num = [23,19,56,21,45]
for j in [1,2,3,4]:
    for i in [0,1,2,3]:
        if Num[i]>Num[i+1]:
            a = Num[i]
            Num[i] = Num[i+1]
            Num[i+1] = a
print('the sequence is',Num)

# Example: counting in the loop
Num = [23,19,56,21,45]
count = 0
for num in Num:
    count = count + 1
    print(count,".",num)

# Example: summing in a loop:
Num = [23,19,56,21,45]
zork = 0
for num in Num:
    zork =  zork + num
print('the sum is',zork)

# None; Example: find smallest value ; is/ is not
smallest_so_far = None
Num = [23,19,56,21,45]
for num in Num:
    if smallest_so_far is None:
        smallest_so_far = num
    elif smallest_so_far > num:
        smallest_so_far = num
print('the smallest number is ',smallest_so_far)
