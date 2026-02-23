import sys

Ax, Ay = map(float, sys.stdin.readline().split())
Bx, By = map(float, sys.stdin.readline().split())

# B' is reflection of B across x-axis
Bx2, By2 = Bx, -By

# If line AB' is horizontal (Ay == By2), it never hits y=0 unless Ay==0
# But for valid testcases, intersection exists and is unique.
t = -Ay / (By2 - Ay)   # solve Ay + t*(By2 - Ay) = 0
Px = Ax + t * (Bx2 - Ax)
Py = 0.0

print(f"{Px:.10f} {Py:.10f}")