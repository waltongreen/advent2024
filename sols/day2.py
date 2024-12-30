# f = open("../data/day2_test_data.txt", "r")
f = open("../data/day2_data.txt", "r")

data=f.read().split('\n')
s=0

def is_safe(xint):
    acc=[1,2,3]
    acc2=[-1,-2,-3]
    xint_shift=xint[1:]
    diff=[x-y for x,y in zip(xint[:-1],xint_shift)]
    if all(d in acc for d in diff) or all(d in acc2 for d in diff):
        return True
    else:
        return False


# PART ONE
for x in data:
    if x != '':
        xint=[int(i) for i in x.split(" ")]
        if is_safe(xint):
            s=s+1

print("Part one Answer: " + str(s))

# PART TWO
s=0
for x in data:
    if x != '':
        xint=[int(i) for i in x.split(" ")]
        if is_safe(xint):
             s=s+1
        else:
            i=0
            t=s
            while i != len(xint) and s == t:
                 xsub=xint[:i]+xint[i+1:]
                 if is_safe(xsub):
                     s=s+1
                 i=i+1

print("Part two Answer: " + str(s))

