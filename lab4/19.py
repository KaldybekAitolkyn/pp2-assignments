import math

def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def dist_origin_to_segment(A, B):
    dx, dy = B[0] - A[0], B[1] - A[1]
    a = dx*dx + dy*dy
    if a == 0.0:
        return math.hypot(A[0], A[1])
    t = - (A[0]*dx + A[1]*dy) / a
    if t < 0.0: t = 0.0
    elif t > 1.0: t = 1.0
    cx, cy = A[0] + t*dx, A[1] + t*dy
    return math.hypot(cx, cy)

def tangent_angles_and_len(P, R):
    x, y = P
    d = math.hypot(x, y)
    base = math.atan2(y, x)
    if abs(d - R) < 1e-12:
        return [base], 0.0
    off = math.acos(R / d)
    tlen = math.sqrt(d*d - R*R)
    return [base + off, base - off], tlen

def min_abs_angle_diff(a, b):
    twopi = 2.0 * math.pi
    d = (a - b) % twopi
    if d > math.pi:
        d -= twopi
    return abs(d)

R = float(input().strip())
A = tuple(map(float, input().split()))
B = tuple(map(float, input().split()))

eps = 1e-12
if dist_origin_to_segment(A, B) >= R - eps:
    print(f"{dist(A, B):.10f}")
else:
    angA, lenA = tangent_angles_and_len(A, R)
    angB, lenB = tangent_angles_and_len(B, R)

    best = float("inf")
    for a in angA:
        for b in angB:
            arc = R * min_abs_angle_diff(a, b)
            best = min(best, lenA + lenB + arc)

    print(f"{best:.10f}")