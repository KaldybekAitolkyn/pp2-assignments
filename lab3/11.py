class Pair:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Pair(new_a, new_b)


# -------- INPUT --------
a1, b1, a2, b2 = map(int, input().split())

# екі объект
p1 = Pair(a1, b1)
p2 = Pair(a2, b2)

# қосу
result = p1.add(p2)

# шығару
print("Result:", result.a, result.b)

