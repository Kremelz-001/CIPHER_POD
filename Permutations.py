import cProfile


def faculty(n):
    if(n<=1 or n==0):
        return 1
    else:
        return faculty(n-1)*n



def counter(n):
    c=0
    for i in range(n):
        c+=1
    return c
cProfile.run('counter(faculty(14))')