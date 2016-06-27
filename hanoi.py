def move(n, source, target, reserve):
    if n > 0:
        move(n-1, source, reserve, target)
        if source:
            target.append(source.pop())
        move(n-1, reserve, target, source)

source = [4, 3, 2, 1]
target = []
reserve = []
move(len(source), source, target, reserve)
print source, target, reserve