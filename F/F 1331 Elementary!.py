# https://codeforces.com/problemset/problem/1331/F

def isElementary(string, ele, i=0):
    if i >= len(string):
        return True
    elif string[i] in ele and isElementary(string, ele, i+1):
        return True
    elif string[i:i+2] in ele and isElementary(string, ele, i+2):
        return True
    else:
        return False

def main():
    s = input()
    ele = 'H He He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og'
    ele = [str(e).upper() for e in ele.split()]

    if isElementary(s, ele):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
