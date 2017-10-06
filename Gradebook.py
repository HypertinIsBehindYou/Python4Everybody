"""
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
"""

score = input("Enter Score: ")

try:
    s = float(score)
except:
    print("please enter numeric numbers")
    quit()

if s>1.0 or s< 0.0:
    print("value out of range! please enter number btw 1.0 and 0.0")
elif s >= 0.9:
    print("A")
elif s >=0.8:
    print("B")
elif  s >=0.7:
    print("C")
elif  s >=0.6:
    print("D")
else:
    print("F")
