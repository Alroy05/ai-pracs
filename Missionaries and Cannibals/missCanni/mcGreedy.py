from queue import PriorityQueue

class State:
    def __init__(self, m, c, b):
        self.m = m  # number of missionaries on the starting bank
        self.c = c  # number of cannibals on the starting bank
        self.b = b  # 1 if boat is on starting bank, 0 if on other bank

    def is_valid(self):
        if self.m < 0 or self.c < 0 or self.m > 3 or self.c > 3:
            return False
        if self.m < self.c and self.m > 0:
            return False
        if 3 - self.m < 3 - self.c and 3 - self.m > 0:
            return False
        return True

    def is_goal(self):
        return self.m == 0 and self.c == 0 and self.b == 0

    def __eq__(self, other):
        return self.m == other.m and self.c == other.c and self.b == other.b

    def __hash__(self):
        return hash((self.m, self.c, self.b))

def h(state):
    """Heuristic function: returns the number of missionaries and cannibals remaining on the starting bank"""
    return state.m + state.c

def get_successors(state):
    successors = []
    if state.b == 1:
        successors += [State(state.m - 1, state.c, 0),
                       State(state.m - 2, state.c, 0),
                       State(state.m, state.c - 1, 0),
                       State(state.m, state.c - 2, 0),
                       State(state.m - 1, state.c - 1, 0)]
    else:
        successors += [State(state.m + 1, state.c, 1),
                       State(state.m + 2, state.c, 1),
                       State(state.m, state.c + 1, 1),
                       State(state.m, state.c + 2, 1),
                       State(state.m + 1, state.c + 1, 1)]
    return [s for s in successors if s.is_valid()]

def best_first_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((h(initial_state), initial_state))
    came_from = {}
    came_from[initial_state] = None

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state.is_goal():
            break

        for next_state in get_successors(current_state):
            if next_state not in came_from:
                came_from[next_state] = current_state
                frontier.put((h(next_state), next_state))

    return came_from

def reconstruct_path(came_from, goal):
    current = goal
    path = []
    while current:
        path.append(current)
        current = came_from[current]
    return path[::-1]

def solve():
    initial_state = State(3, 3, 1)
    came_from = best_first_search(initial_state)
    goal_state = State(0, 0, 0)
    path = reconstruct_path(came_from, goal_state)
    for i, state in enumerate(path):
        print(f"Step {i + 1}: (M={state.m}, C={state.c}, B={'left' if state.b == 1 else 'right'})")

if __name__ == "__main__":
    solve()
