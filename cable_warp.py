import sys
from collections import deque

def solve():
    try:
        # Reading N and M
        N, M = map(int, sys.stdin.readline().split())
    except (EOFError, ValueError):
        return 

    # Reading the grid
    grid = []
    for _ in range(N):
        grid.append(sys.stdin.readline().split())

    #Helper Functions 

    def is_in_bounds(r, c):
        """Checking if (r, c) is inside the grid."""
        return 0 <= r < N and 0 <= c < M

    def get_neighbors(r, c):
        """Get valid neighbors (up, down, left, right)."""
        neighbors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if is_in_bounds(nr, nc):
                neighbors.append((nr, nc))
        return neighbors

    def has_neighbor(r, c, char_type):
        """Checking if (r, c) has an adjacent cell of char_type."""
        for nr, nc in get_neighbors(r, c):
            if grid[nr][nc] == char_type:
                return True
        return False

    def is_rod_component(r, c):
        if grid[r][c] == 'R':
            return True
        if grid[r][c] == 'C' and has_neighbor(r, c, 'R'):
            return True
        return False

    def is_intersection(r, c):
        
        if not is_rod_component(r, c):
            return False
        
        # Checking if this rod part has a cable neighbor
        return has_neighbor(r, c, 'C')

    #Main 
    total_switches = 0
    visited = set()

    for r in range(N):
        for c in range(M):
            
            if (r, c) not in visited and is_rod_component(r, c):
                
               
                rod_cells_this_rod = []
                q = deque([(r, c)])
                visited.add((r, c))

                rod_over_count = 0
                cable_over_count = 0
                
                #BFS to find all connected rod components
                while q:
                    cr, cc = q.popleft()
                    rod_cells_this_rod.append((cr, cc))

                    # Checking all 4 neighbors
                    for nr, nc in get_neighbors(cr, cc):
                        if (nr, nc) not in visited and is_rod_component(nr, nc):
                            visited.add((nr, nc))
                            q.append((nr, nc))
                
                
                for rr, cc in rod_cells_this_rod:
                    if is_intersection(rr, cc):
                        if grid[rr][cc] == 'R':
                            rod_over_count += 1
                        elif grid[rr][cc] == 'C':
                            cable_over_count += 1
                
               
                total_switches += min(rod_over_count, cable_over_count)

    print(total_switches)


if __name__ == "__main__":
    solve()
