from collections import deque

# Define the initial state
initial_state = (3, 3, 1)  # (missionaries on left, cannibals on left, boat position)

# Define the goal state
goal_state = (0, 0, 0)  # (all missionaries on right, all cannibals on right, boat on right)

# Function to check if a state is valid
def is_valid(state):
    missionaries_left, cannibals_left, boat = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left
    
    # Check if missionaries are outnumbered by cannibals
    if missionaries_left < cannibals_left and missionaries_left > 0:
        return False
    if missionaries_right < cannibals_right and missionaries_right > 0:
        return False
    
    return True

# Function to generate next valid states
def next_states(state):
    possible_moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    moves = []
    missionaries_left, cannibals_left, boat = state
    
    if boat == 1:
        for move in possible_moves:
            missionaries_new = missionaries_left - move[0]
            cannibals_new = cannibals_left - move[1]
            if 0 <= missionaries_new <= 3 and 0 <= cannibals_new <= 3 and is_valid((missionaries_new, cannibals_new, 0)):
                moves.append((missionaries_new, cannibals_new, 0))
    else:
        for move in possible_moves:
            missionaries_new = missionaries_left + move[0]
            cannibals_new = cannibals_left + move[1]
            if 0 <= missionaries_new <= 3 and 0 <= cannibals_new <= 3 and is_valid((missionaries_new, cannibals_new, 1)):
                moves.append((missionaries_new, cannibals_new, 1))
    return moves

# Breadth-first search to find solution
def bfs():
    visited = set()
    queue = deque([(initial_state, [])])  # Queue of states and their path
    
    while queue:
        state, path = queue.popleft()
        visited.add(state)
        
        if state == goal_state:
            return path
        
        for next_state in next_states(state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))
                visited.add(next_state)
    
    return None

# Find solution
solution = bfs()

# Print solution
if solution:
    print("Solution found:")
    for i, state in enumerate(solution):
        print(f"Step {i + 1}: {state}")
else:
    print("No solution found.")
