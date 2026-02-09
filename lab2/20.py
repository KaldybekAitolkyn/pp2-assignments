n = int(input())
db = {}

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == "set":
        key = cmd[1]
        value = cmd[2]
        db[key] = value
    else:  # get
        key = cmd[1]
        if key in db:
            print(db[key])
        else:
            print(f"KE: no key {key} found in the document")
