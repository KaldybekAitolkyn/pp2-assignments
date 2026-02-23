import json
import re

token_re = re.compile(r'\.([A-Za-z_]\w*)|\[([0-9]+)\]|^([A-Za-z_]\w*)')

def eval_query(data, q):
    pos = 0
    cur = data

    while pos < len(q):
        m = token_re.match(q, pos)
        if not m:
            return None, False

        key1 = m.group(1) or m.group(3)
        idx = m.group(2)

        if key1 is not None:
            if not isinstance(cur, dict) or key1 not in cur:
                return None, False
            cur = cur[key1]
        else:
            i = int(idx)
            if not isinstance(cur, list) or i < 0 or i >= len(cur):
                return None, False
            cur = cur[i]

        pos = m.end()

    return cur, True

data = json.loads(input().strip())
qnum = int(input().strip())

for _ in range(qnum):
    q = input().strip()
    val, ok = eval_query(data, q)
    if not ok:
        print("NOT_FOUND")
    else:
        print(json.dumps(val, separators=(",", ":"), ensure_ascii=False, sort_keys=True))