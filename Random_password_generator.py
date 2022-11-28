#Random Password generator

import random
passlen=int(input("Enter the length of password"))
s="abcdefghijklmnopqrtsuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p=  "".join(random.sample(s,passlen))
print(p)
