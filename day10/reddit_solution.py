import sys
from itertools import combinations_with_replacement
import re
import scipy.optimize

nre = re.compile(r'(\d+)')
def GetNums(x):
    return list(map(int, nre.findall(x)))

L = sys.stdin.read().strip().split('\n')
lightsre = re.compile(r'[.#]+')
bre = re.compile(r'\([^)]+\)')
jre =re.compile(r'\{[^}]+\}')
Lights = []
Buttons = []
Jolts = []
for num,l in enumerate(L):
    ls = lightsre.findall(l)[0]
    lights = [ll == '#' for ll in ls]
    Lights.append(lights)

    bs = bre.findall(l)
    B = []
    for b in bs:
        B.append(GetNums(b))
    Buttons.append(B)

    js = jre.findall(l)[0]
    Jolts.append(GetNums(js))

count = 0
for n in range(len(L)):
    wanted = Lights[n]
    have = None
    picks = 0
    while have != wanted:
        picks += 1
        for bs in combinations_with_replacement(Buttons[n], picks):
            have = [False]*len(wanted)
            for b in bs:
                for bb in b:
                    have[bb] ^= True
            if have == wanted:
                count += picks
                break
print(count)

def Solve(want, buttons_arr):
    A = []
    #For every index, does this button have an effect?
    #Creating an array of buttons for each light
    for n in range(len(want)):
        arr = []
        for buttons in buttons_arr:
            if n in buttons:
                arr.append(1)
            else:
                arr.append(0)
        A.append(arr)

    bob = scipy.optimize.linprog([1]*len(buttons_arr),
                                 A_eq=A,
                                 b_eq=want,
                                 bounds=(0, None),
                                 method="highs",
                                 integrality=1)

    return round(bob.fun)

count = 0
for n in range(len(L)):
    count += Solve(Jolts[n], Buttons[n])
print(count)