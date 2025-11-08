import sys
import copy
from collections import deque, Counter

# N will be set from input
N = 0

# --- Helper Functions for Cube Operations ---

def rotate_face(face, direction):
    """Rotates a single N x N face clockwise ('right') or counter-clockwise ('left')."""
    new_face = [[None for _ in range(N)] for _ in range(N)]
    if direction == 'right': # Clockwise
        for r in range(N):
            for c in range(N):
                new_face[c][N-1-r] = face[r][c]
    elif direction == 'left': # Counter-clockwise
        for r in range(N):
            for c in range(N):
                new_face[N-1-c][r] = face[r][c]
    return new_face

def execute_instruction(cube_state, instruction_str):
    """
    Mutates the cube_state dictionary based on the given instruction.
    Rules 1-6 are whole-cube rotations.
    Rule 7 is a single-face, single-row/col circular shift.
    """
    parts = instruction_str.split()
    
    # Rules 1-6: Whole-cube rotations
   
    if parts[0] == 'turn':
        new_state = {}
        if parts[1] == 'left':
            # front(4) -> left(5), left(5) -> back(2), back(2) -> right(6), right(6) -> front(4)
            new_state[5] = cube_state[4]
            new_state[2] = cube_state[5]
            new_state[6] = cube_state[2]
            new_state[4] = cube_state[6]
            new_state[3] = rotate_face(cube_state[3], 'right') # top
            new_state[1] = rotate_face(cube_state[1], 'left')  # base
            cube_state.update(new_state)
        elif parts[1] == 'right':
            # front(4) -> right(6), right(6) -> back(2), back(2) -> left(5), left(5) -> front(4)
            new_state[6] = cube_state[4]
            new_state[2] = cube_state[6]
            new_state[5] = cube_state[2]
            new_state[4] = cube_state[5]
            new_state[3] = rotate_face(cube_state[3], 'left')  # top
            new_state[1] = rotate_face(cube_state[1], 'right') # base
            cube_state.update(new_state)
            
    elif parts[0] == 'rotate':
        new_state = {}
        if parts[1] == 'front':
            # 4 -> 1, 1 -> 2, 2 -> 3, 3 -> 4
            new_state[1] = cube_state[4]
            new_state[2] = cube_state[1]
            new_state[3] = cube_state[2]
            new_state[4] = cube_state[3]
            new_state[5] = rotate_face(cube_state[5], 'right') # left
            new_state[6] = rotate_face(cube_state[6], 'left')  # right
            cube_state.update(new_state)
        elif parts[1] == 'back':
            # 4 -> 3, 3 -> 2, 2 -> 1, 1 -> 4
            new_state[3] = cube_state[4]
            new_state[2] = cube_state[3]
            new_state[1] = cube_state[2]
            new_state[4] = cube_state[1]
            new_state[5] = rotate_face(cube_state[5], 'left')  # left
            new_state[6] = rotate_face(cube_state[6], 'right') # right
            cube_state.update(new_state)
        elif parts[1] == 'left':
            # 3 -> 5, 5 -> 1, 1 -> 6, 6 -> 3
            new_state[5] = cube_state[3]
            new_state[1] = cube_state[5]
            new_state[6] = cube_state[1]
            new_state[3] = cube_state[6]
            new_state[4] = rotate_face(cube_state[4], 'left')  # front
            new_state[2] = rotate_face(cube_state[2], 'right') # back
            cube_state.update(new_state)
        elif parts[1] == 'right':
            # 3 -> 6, 6 -> 1, 1 -> 5, 5 -> 3
            new_state[6] = cube_state[3]
            new_state[1] = cube_state[6]
            new_state[5] = cube_state[1]
            new_state[3] = cube_state[5]
            new_state[4] = rotate_face(cube_state[4], 'right') # front
            new_state[2] = rotate_face(cube_state[2], 'left')  # back
            cube_state.update(new_state)

    # Rule 7: Single-face row/col shift
    else:
        face_map = {'base': 1, 'back': 2, 'top': 3, 'front': 4, 'left': 5, 'right': 6}
        face_name = parts[0]
        face_num = face_map[face_name]
        idx = int(parts[1]) - 1 # 0-indexed
        direction = parts[2]
        
        target_face = cube_state[face_num]
        
        if direction == 'left' or direction == 'right':
            # Row shift
            row_deque = deque(target_face[idx])
            shift = -1 if direction == 'left' else 1
            row_deque.rotate(shift)
            target_face[idx] = list(row_deque)
            
        elif direction == 'up' or direction == 'down':
            # Column shift
            col = [target_face[r][idx] for r in range(N)]
            col_deque = deque(col)
            shift = -1 if direction == 'up' else 1
            col_deque.rotate(shift)
            shifted_col = list(col_deque)
            for r in range(N):
                target_face[r][idx] = shifted_col[r]

# --- Solver Functions ---

def is_solved(cube):
    """Checks if any face is perfectly solved."""
    for face_num in range(1, 7):
        face = cube[face_num]
        color = face[0][0]
        if all(face[r][c] == color for r in range(N) for c in range(N)):
            return True
    return False

def is_faulty_solved(cube):
    """Checks if any face is solved *except* for one sticker."""
    for face_num in range(1, 7):
        face = cube[face_num]
        counts = Counter()
        for r in range(N):
            for c in range(N):
                counts[face[r][c]] += 1
        
        # Check if any color count is (N*N - 1)
        for count in counts.values():
            if count == (N*N - 1):
                return True
    return False

def solve():
    global N
    try:
        n_str, k_str = sys.stdin.readline().split()
        N = int(n_str)
        K = int(k_str)
    except:
        return # Handle empty input

    # Read all 6 faces
    original_cube = {}
    for face_num in range(1, 7):
        face = []
        for _ in range(N):
            face.append(sys.stdin.readline().split())
        original_cube[face_num] = face
    
    # Read all K instructions
    instructions = []
    for _ in range(K):
        instructions.append(sys.stdin.readline().strip())

    # --- Tier 1: Check for a "Not Faulty" solution ---
   
    for i in range(K):
        cube_copy = copy.deepcopy(original_cube)
        skipped_instruction = instructions[i]
        
        # Loop 'j' executes the other K-1 instructions
        for j in range(K):
            if i == j:
                continue
            execute_instruction(cube_copy, instructions[j])
        
        if is_solved(cube_copy):
            print(skipped_instruction)
            return

    # --- Tier 2: Check for a "Faulty" solution ---

    for i in range(K):
        cube_copy = copy.deepcopy(original_cube)
        skipped_instruction = instructions[i]
        
        for j in range(K):
            if i == j:
                continue
            execute_instruction(cube_copy, instructions[j])
        
        if is_faulty_solved(cube_copy):
            print("Faulty")
            print(skipped_instruction)
            return

    # --- Tier 3: No solution found ---
    print("Not Possible")

# --- Run the solver ---
if __name__ == "__main__":
    solve()
