n=int(input())
words=input().split()
results=[]
for i, word in enumerate(words):
    results.append(str(i)+":"+word)
print(" ".join(results))
