trip_to_digit = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

digit_to_trip = {v: k for k, v in trip_to_digit.items()}


def decode(s):  # "ONETWO" -> 12
    digits = []
    for i in range(0, len(s), 3):
        digits.append(trip_to_digit[s[i:i+3]])
    return int("".join(digits))


def encode(num):  # 12 -> "ONETWO"
    if num == 0:
        return "ZER"
    res = []
    for ch in str(num):
        res.append(digit_to_trip[ch])
    return "".join(res)


expr = input().strip()

# табамыз қай оператор тұр
op = None
for sym in "+-*":
    if sym in expr:
        op = sym
        left, right = expr.split(sym)
        break

a = decode(left)
b = decode(right)

if op == "+":
    ans = a + b
elif op == "-":
    ans = a - b
else:  # "*"
    ans = a * b

# егер минус шығуы мүмкін болса (кей платформаларда болады)
if ans < 0:
    print("-" + encode(-ans))
else:
    print(encode(ans))
