movie_idx = {}
f = open('movie_ids.txt',encoding= 'gbk')
for line in f:
    tokens = line.split(' ')
    tokens[-1] = tokens[-1][:-1]    #去换行符
    movie_idx[int(tokens[0]) - 1] = ' '.join(tokens[1:])

print(movie_idx)