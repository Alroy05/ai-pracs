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


def dfs(state, visited, path):
    visited.add(state)
    path.append(state)
    if state.is_goal():
        return True
    for successor in get_successors(state):
        if successor not in visited:
            if dfs(successor, visited, path):
                return True
    path.pop()
    return False


def solve():
    initial_state = State(3, 3, 1)
    visited = set()
    path = []
    if dfs(initial_state, visited, path):
        for i, state in enumerate(path):
            print(f"Step {i + 1}: (M={state.m}, C={state.c}, B={'left' if state.b == 1 else 'right'})")
    else:
        print("No solution found.")


if __name__ == "__main__":
    solve()
