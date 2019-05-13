# if ~ else

a = 10
if a > 5:
    print('big')

a = 3
if a > 5:
    print('big')
else:
    print('small')

# if ~ elif ~ else
n = 0

if n > 0:
    print('양수')
elif n < 0:
    print('음수')
else:
    print('0')


#  spam : 100
#  egg : 500
# spagetti : 2000

price = 0
goods = 'spagetti'

if goods == 'spam':
    price = 100
elif goods == 'egg':
    price = 500
elif goods == 'spagetti':
    price = 2000

print(price)

# 삼항 연산자
#
#   print( a > 5 ? 'big' : 'small' )
#
a = 10
print('big' if a > 5 else 'small')



