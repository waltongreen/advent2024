# f = open("../data/day1_test_data.txt", "r")
f = open("../data/day1_data.txt", "r")

data=f.read()

full=list(int(i) for i in data.split())
a=full[::2]
b=full[1::2]

a.sort()
b.sort()

l=len(a)

# PART ONE
ans=0
for i in range(0,l):
    ans=ans+abs(a[i]-b[i])
print("Part One Answer: " + str(ans))

# PART TWO
ss=0
while len(a)*len(b) != 0:
    x=a[0]
    y=b[0]
    if x < y:
        # delete first element of a
        del a[0]
    elif x > y:
        # delete first element of b
        del b[0]
    else:
        # count number of occurences of x in a
        #   using that a is sorted
        j=0 # counter for a
        i=0 # iterate
        look=x
        while look == x:
            j=j+1
            i=i+1
            if i == len(a):
                look=x+1
            else:
                look=a[i]
        # count number of occurences of y in b
        #   using that b is sorted
        k=0 # counter for b
        i=0 # iterate
        look=y
        while look == y:
            k=k+1
            i=i+1
            if i == len(b):
                look=y+1 # this should exit the while loop
            else:
                look=b[i]
        # increase score
        ss=ss+j*k*x
        del a[0:j]
        del b[0:k]

print("Part Two Answer: " + str(ss))
