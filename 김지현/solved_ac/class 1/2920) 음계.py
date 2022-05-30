ascending = '12345678'
scale = input().replace(" ", "")

if scale == ascending:
    print('ascending')
elif scale == ascending[::-1]:
    print('descending')
else:
    print('mixed')