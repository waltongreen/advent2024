# f = open("../data/day4_test_data.txt", "r")
f = open("../data/day4_data.txt", "r")

data=f.read().split("\n")
# delete final empty line
del data[-1]
n=len(data)
m=len(data[0])


def read_nbrs(i,j,l):
    # this returns the 4 strings passing through data[i][j] of length 2l+1
    intersecs=[['' for k in range(0,2*l+1)]for k in range(0,4)]
    for k in range(0,2*l+1):
        if j-l+k in range(0,m):
            intersecs[0][k]=data[i][j-l+k] # west to east
        else:
            intersecs[0][k]=' '
        if i-l+k in range(0,n):
            intersecs[1][k]=data[i-l+k][j] # north to south
        else:
            intersecs[1][k]=' '
        if j-l+k in range(0,m) and i-l+k in range(0,n):
            intersecs[2][k]=data[i-l+k][j-l+k] # northwest to southeast
        else:
            intersecs[2][k]=' '
        if j-l+k in range(0,m) and i-k+l in range(0,n):
            intersecs[3][k]=data[i-k+l][j-l+k] # southwest to northeast
        else:
            intersecs[3][k]=' '
    return[''.join(intersec) for intersec in intersecs]

def count_XMAS(data):
    s=0
    for d in data:
        s=s+d.count("XMAS")+d.count("SAMX")
    return s

def is_X_MAS(intersecs):
    key=['MAS','SAM']
    return intersecs[2] in key and intersecs[3] in key


# PART ONE
s=0
for i in range(0,n):
    for j in range(0,m):
        if data[i][j] == 'X':
            s=s+count_XMAS(read_nbrs(i,j,3))

print("Part one Answer: " + str(s))

# PART TWO
s=0
for i in range(0,n):
    for j in range(0,m):
        if data[i][j] == 'A' and is_X_MAS(read_nbrs(i,j,1)):
            s=s+1

print("Part two Answer: " + str(s))

