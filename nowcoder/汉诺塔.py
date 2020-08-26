def move(n,start,mid,end):
    if n == 1:
        print('{}-->{}'.format(start, end))
        return
    else:
        move(n-1,start,end,mid)
        print('{}-->{}'.format(start, end))
        move(n-1,mid,start,end)

move(3, 'a', 'b', 'c')