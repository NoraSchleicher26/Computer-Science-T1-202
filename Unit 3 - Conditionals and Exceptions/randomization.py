import random

r = random.randrange(0,10)
# ) is INCLUSIVE and the 10 is EXCLUSIVE
# 0 <= result < 10
print(r)

p = random.random()
if p < 0.25:
    print("SUCCESS")
else:
    print("FAIL")
