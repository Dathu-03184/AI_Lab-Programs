import itertools

# Distance matrix (symmetric)
# Example: 4 cities (0, 1, 2, 3)
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

N = len(distance)
cities = list(range(N))

min_cost = float('inf')
best_path = None

for perm in itertools.permutations(cities[1:]):  # fix starting city as 0
    current_cost = 0
    path = [0] + list(perm) + [0]

    for i in range(len(path)-1):
        current_cost += distance[path[i]][path[i+1]]

    if current_cost < min_cost:
        min_cost = current_cost
        best_path = path

print("Best path:", best_path)
print("Minimum cost:", min_cost)
