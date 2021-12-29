empty = set()

empty.add(4)
empty.add(5)
print(empty)

empty.add((8,9,10))
print(empty)

print(len(empty))
empty.remove(5)
print(empty)
empty.pop()
print(empty)