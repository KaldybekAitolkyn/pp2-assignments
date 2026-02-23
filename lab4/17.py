import math

def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]

R = float(input().strip())
Ax, Ay = map(float, input().split())
Bx, By = map(float, input().split())

A = (Ax, Ay)
B = (Bx, By)
d = (B[0] - A[0], B[1] - A[1])

seg_len = math.hypot(d[0], d[1])
if seg_len == 0.0:
    # A == B (trajectory length is 0 anyway)
    print(f"{0.0:.10f}")
    raise SystemExit

a = dot(d, d)
b = 2.0 * dot(A, d)
c = dot(A, A) - R*R

D = b*b - 4*a*c

def clamp01(x):
    return max(0.0, min(1.0, x))

inside_len = 0.0

if D < 0:
    # no intersection with boundary
    if c <= 0:
        inside_len = seg_len  # whole segment inside
    else:
        inside_len = 0.0      # whole segment outside
else:
    sqrtD = math.sqrt(D)
    t1 = (-b - sqrtD) / (2*a)
    t2 = (-b + sqrtD) / (2*a)
    t_low, t_high = (t1, t2) if t1 <= t2 else (t2, t1)

    # inside part is intersection of [t_low, t_high] with [0, 1]
    L = max(0.0, min(1.0, t_high) - max(0.0, t_low))
    inside_len = seg_len * L

print(f"{inside_len:.10f}")