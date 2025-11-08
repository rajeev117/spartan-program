import sys

def solve():
    """
    Determines the number of cut and insert operations required by finding
    the Longest "Run" Subsequence (LCS-Run).
    
    This is N - L', where L' is the length of the longest subsequence
    of consecutive original indices (e.g., 2, 3, 4).
    """

    # --- Input Reader ---
    try:
        n_instr = sys.stdin.readline().strip()
        if not n_instr:
            return
        N = int(n_instr)
    except(EOFError,ValueError):
        return

    if N == 0:
        print(0)
        return

    sys.stdin.readline() # Skips "shuffled"
    shuffled_instr = []
    for _ in range(N):
        shuffled_instr.append(sys.stdin.readline().strip())

    sys.stdin.readline() # Skips "original"

    og_instr = []
    for _ in range(N):
        og_instr.append(sys.stdin.readline().strip())

    # --- Map Original Order and Convert Shuffled List ---
    og_index_map = {
        instruction:i
        for i, instruction in enumerate(og_instr)
    }

    index_sequence = [
        og_index_map[instruction]
        for instruction in shuffled_instr
    ]
    
    # --- Find the Longest "Run" Subsequence (LCS-Run) ---
    
    # We use a map (dictionary) to store the length
    # of the run *ending* with a specific index value.
    # dp[k] = length of the longest run ending with index k
    
    dp = {} 
    max_run_len = 0
    
    if N == 0:
        print(0)
        return

    for val in index_sequence:
        # Check if the previous number (val - 1) is in our map.
        if val - 1 in dp:
            # If it is, this new 'val' extends the run.
            dp[val] = dp[val - 1] + 1
        else:
            # If not, this 'val' starts a new run of length 1.
            dp[val] = 1
        
        # Update the overall maximum length found.
        max_run_len = max(max_run_len, dp[val])

    # --- Result Calculation ---
    min_operations = N - max_run_len
    
    print(min_operations)

if __name__ == '__main__':
    solve()
