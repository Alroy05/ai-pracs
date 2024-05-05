import random

def initial_state(N):
    """Generate a random initial state."""
    return [random.randint(0, N-1) for _ in range(N)]

def num_attacks(state):
    """Calculate the number of attacks (conflicts) in the current state."""
    N = len(state)
    attacks = 0
    for i in range(N):
        for j in range(i+1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks

def hill_climbing(N, max_iter=1000000):
    """Hill-climbing algorithm to solve N-Queens problem."""
    current_state = initial_state(N)
    current_attacks = num_attacks(current_state)

    for _ in range(max_iter):
        if current_attacks == 0:
            return current_state  # Solution found
        neighbors = []
        for i in range(N):
            for j in range(N):
                if j != current_state[i]:
                    neighbor_state = list(current_state)
                    neighbor_state[i] = j
                    neighbors.append((neighbor_state, num_attacks(neighbor_state)))
        neighbors.sort(key=lambda x: x[1])
        if neighbors[0][1] >= current_attacks:
            break  # Local minimum reached
        current_state, current_attacks = neighbors[0]

    return None  # Failed to find a solution

def print_solution(solution):
    """Print the N-Queens solution."""
    if solution is None:
        print("Failed to find a solution.")
    else:
        for row_index, row in enumerate(solution):
            print(" ".join('Q' if col == row else '.' for col in range(len(solution))))


if __name__ == "__main__":
    N = 4  # Change N for different board sizes
    solution = hill_climbing(N)
    print("Solution:")
    print_solution(solution)
