import sys

def solve():
    m = int(sys.stdin.readline().strip())
    g = 0

    def outer():
        n = 0

        def inner():
            nonlocal n
            global_dummy = None  # not used, just to show local exists
            local_x = 0

            nonlocal_g = 0  # we'll update g via enclosing solve() variable

            # We'll capture g from solve() using a mutable container
            return

        return n

    # easier: just simulate scopes with two accumulators
    n = 0
    for _ in range(m):
        scope, val = sys.stdin.readline().split()
        val = int(val)
        if scope == "global":
            g += val
        elif scope == "nonlocal":
            n += val
        else:  # local
            pass

    print(g, n)

if __name__ == "__main__":
    solve()