lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
a = []
for i in lowercase:
    for j in lowercase:
        for k in digits:
            for l in digits:
                #'{}{}{}{}'.format(i,j,k,l)
                (i + j + k + l)

answer = [i+j+k+l for i in lowercase for j in lowercase for k in digits for l in digits]