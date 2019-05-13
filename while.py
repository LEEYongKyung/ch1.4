# while

count = 1
while count < 5:
    print(count)
    count += 1

# 1 ~ 10
s, i = 0, 1
while i <= 10:
    s += i
    i += 1

print(s)


# break, continue, else 문 적용
i = 0
while i < 10:
    i += 1
    if i < 5:
        continue

    print(i, end=' ')

    if i > 10:
        break
else:
    print('else block')

# 무한루프
i = 0
while True:
    print(i, end=' ')
    if i > 5000:
        break
    i += 1
else:
    print('else block')

