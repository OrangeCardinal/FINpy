import math

def cubic_roots(a, b, c, d, xl, xh):
    """
    ==============
    = References =
    ==============
    https://en.wikipedia.org/wiki/Cube_root

    :param a:
    :param b:
    :param c:
    :param d:
    :param xl:
    :param xh:
    :return:
    """
    if a != 0:
        roots = []
        aa = a
        a = b / aa
        b = c / aa
        c = d / aa
        q = (a * a - 3 * b) / 9.0
        r = (2 * a * a * a - 9.0 * a * b + 27.0 * c) / 54.0
        q3 = q * q * q
        diff = r * r - q3
        if diff <=0:
            ratio = r / math.sqrt(q3)
            theta = math.acos(ratio)
            qr = -2.0 * math.sqrt(q)
            a_over_3 = a / 3.0
            r1 = qr * math.cos(theta / 3.0) - a_over_3
            r2 = qr * math.cos((theta + 2.0 * math.pi) / 3.0) - a_over_3
            r3 = qr * math.cos((theta - 2.0 * math.pi) / 3.0) - a_over_3
            rs = [r1, r2, r3]
            rs.sort()
            [r1, r2, r3] = rs
            if r1 >= xl and r1 <= xh:
                roots.append(r1)
            if r2 != r1 and r2 >= xl and r2 <= xh:
                roots.append(r2)
            if r3 != r1 and r3 != r2 and r3 >= xl and r3 <= xh:
                roots.append(r3)
        else:
            if r > 0:
                big_a = -math.pow(r + math.sqrt(diff), 1.0 / 3.0)
            else:
                big_a = math.pow(-r + math.sqrt(diff), 1.0 / 3.0)
            big_b = 0.0

            if big_a != 0: 
                big_b = q / big_a
            r1 = (big_a + big_b) - a / 3.0
            if r1 >= xl and r1 <= xh:
                roots.append(r1)
                return roots
            else:
                return quadratic_roots(b, c, d, xl, xh)
    
def cubic_spline():
    pass

def loglinear():
    pass


def quadratic_roots(a,b,c,x1,xh):
    roots = []
    d = b * b - 4 * a * c
    d = b * b - 4 * a * c
    if d > 0:
        r1 = 0
        r2 = 0
        if a != 0:
            sgn = 1
        if b < 0:
            sgn = -1
            q = -0.5 * (b + sgn * math.sqrt(d))
"""
import math
def quadratic
roots(a, b, c, xl, xh):
# find roots
roots = []
d = b*b-4*a*c
if d > 0:
r1 = 0
r2 = 0
if a
<
>0:
sgn = 1
if b
<
0: sgn = -1
q = -0.5*(b+sgn*math.sqrt(d))
Basic Mathematical Tools
47
r1 = q/a
r2=r1
if q
<
>0:r2=c/q
else:
r1 = -c/b
r2=r1
# order roots
if r1 > r2:
tmp=r1
r1=r2
r2 = tmp
if r1 >= xl and r1
<
= xh:
roots.append(r1)
if r2
<
> r1 and r2 >= xl and r2
<
= xh:
roots.append(r2)
else:
if a
<
>0:
r1 = -b/(2*a)
if r1 >= xl and r1
<
= xh:
roots.append(r1)
return roots
"""