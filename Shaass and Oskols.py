n = int(input())  # Number of wires
birds = list(map(int, input().split()))  # Number of birds on each wire
m = int(input())  # Number of shots

for _ in range(m):
    x, y = map(int, input().split())  # Shot at wire x (1-based index), yth bird
    x -= 1  # Convert to 0-based index

    if x > 0:  # Birds move to the left wire
        birds[x - 1] += y - 1

    if x < n - 1:  # Birds move to the right wire
        birds[x + 1] += birds[x] - y

    birds[x] = 0  # The hit wire loses all birds

# Print the final state
for b in birds:
    print(b)