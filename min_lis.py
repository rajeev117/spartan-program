import sys

def solve():
    """determines the number of cut and insert required by finding LIS"""

    #input reader
    try:
        n_instr=sys.stdin.readline().strip()
        if not n_instr:
            return
        N=int(n_instr)
    except(EOFError,ValueError):
        return

    if N==0:
        print(0)
        return

    sys.stdin.readline()
    shuffled_instr=[]
    for _ in range(N):
        shuffled_instr.append(sys.stdin.readline().strip())

    sys.stdin.readline()

    #reading original intructions
    og_instr=[]
    for _ in range(N):
        og_instr.append(sys.stdin.readline().strip())

    #map original order and covert shuffled list

    og_index_map={
        instruction:i
        for i, instruction in enumerate(og_instr)
    }

    #finding LIS
    index_sequence=[
        og_index_map[instruction]
        for instruction in shuffled_instr
    ]
  
    dp={}
    max_run_len=0
    if N==0:
        print(0)
        return
    for val in index_sequence:
        if val-1 in dp:
            dp[val]=dp[val-1]+1
        else:
            dp[val]=1

        max_run_len=max(max_run_len,dp[val])
        
    #result calculation
    min_operations=N-max_run_len
    print(min_operations)
if __name__=='__main__':
    solve()
