class Solution(object):
    def totalNQueens(self, n):
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        res = [0]  # Use a list to allow modification inside the nested function
        
        def backtrack(r):
            if r == n:
                res[0] += 1
                return
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                backtrack(r + 1)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return res[0]  # Return the result stored in the list
