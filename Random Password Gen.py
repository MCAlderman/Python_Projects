
from random import randint
import random

u_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']


l_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

p_sym = ['!', '@', '#', '$', '%', '&', '*']


num_p_num = 2
num_u_case = 1
num_l_case = 7
num_p_sym = 2

out_pass = []
p = 0
while p < num_p_num:
    out_pass.append(randint(0, 9))
    p += 1

u = 0
while u < num_u_case:
    out_pass.append(u_case[randint(0, len(u_case)-1)])
    u += 1

l = 0
while l < num_l_case:
    out_pass.append(l_case[randint(0, len(l_case)-1)])
    l += 1

s = 0
while s < num_p_sym:
    out_pass.append(p_sym[randint(0, len(p_sym)-1)])
    s += 1

lines = random.sample(range(len(out_pass)), len(out_pass))

fin = 0
fin_pass = [out_pass[x] for x in lines]
print(fin_pass)

