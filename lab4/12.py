import json

MISSING = object()

def to_json(v):
    if v is MISSING:
        return "<missing>"
    return json.dumps(v, separators=(",", ":"), ensure_ascii=False, sort_keys=True)

def deep_diff(a, b, path, out):
    a_is_obj = isinstance(a, dict)
    b_is_obj = isinstance(b, dict)

    if a_is_obj and b_is_obj:
        keys = set(a.keys()) | set(b.keys())
        for k in keys:
            new_path = f"{path}.{k}" if path else k
            av = a.get(k, MISSING)
            bv = b.get(k, MISSING)
            if av is MISSING or bv is MISSING:
                out.append((new_path, av, bv))
            else:
                deep_diff(av, bv, new_path, out)
        return

    if a != b:
        out.append((path, a, b))

a = json.loads(input().strip())
b = json.loads(input().strip())

diffs = []
deep_diff(a, b, "", diffs)

if not diffs:
    print("No differences")
else:
    diffs.sort(key=lambda x: x[0])
    for p, old, new in diffs:
        print(f"{p} : {to_json(old)} -> {to_json(new)}")