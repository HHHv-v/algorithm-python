def count_paths(number,cache):
    if cache<0:
        return 0
    if number in cache:
        return cache[number]
    cache[number]=(
        count_paths(number,cache-1)
        + count_paths(number,cache-2)
        + count_paths(number,cache-3)
    )
    return cache[number]

q=int(input())
cache={0:1}

for _ in range(q):
    number=int(input())
    print(count_paths(number,cache))