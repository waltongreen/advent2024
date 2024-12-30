# f = open("../data/day3_test_data.txt", "r")
# f = open("../data/day3_test_data_part2.txt", "r")
f = open("../data/day3_data.txt", "r")

data=f.read()

def filter_mult(data):
    s=0
    for x in data.split("mul("):
        y=x.split(",")
        if len(y) > 1 and ')' in y[1]: # split(")") does not care if ")" exists or not
            try:
                s=s+int(y[0])*int(y[1].split(")")[0])
            except ValueError:
                pass
    return s

# PART ONE
print("Part one Answer: " + str(filter_mult(data)))

# PART TWO
x=data.split("do()")
s=0
for y in x:
    s=s+filter_mult(y.split("don't()")[0])

print("Part two Answer: " + str(s))

