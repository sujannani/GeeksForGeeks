class Solution:
    def __init__(self):
        self.result = []
        self.row = [0] * 10
    
    def place(self, r, c):
        for prev in range(c):
            if self.row[prev] == r or abs(self.row[prev] - r) == abs(prev - c):
                return False
        return True

    def bt(self, c, n):
        if c == n:
            self.result.append([self.row[i] + 1 for i in range(n)])
            return
        for i in range(n):
            if self.place(i, c):
                self.row[c] = i
                self.bt(c + 1, n)

    def nQueen(self, n):
        self.result = []
        self.bt(0, n)
        return self.result