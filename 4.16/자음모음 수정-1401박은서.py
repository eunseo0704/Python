e, n, space, special, vow, con = 0, 0, 0, 0, 0, 0
vow = 'aeiou'
sen = input()
for i in sen:
    if i.isalpha():
        if i in vow:
            vow += 1
        else:
            con += 1
    elif i.isdight:
        n += 1
    elif i.isspace:
        space += 1
    else:
        special += 1