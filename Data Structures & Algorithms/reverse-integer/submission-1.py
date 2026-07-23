class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x1 = ''
        x2 = ''
        if x[0] == '-':
            x2 = x[0]
            x1 = x[1:]
        if x1 == '':
            x1 = x[::-1]
        else:
            x1 = x1[::-1]
        if int(x1)>(2**31 - 1):
            return 0
        else:
            return int(x2+x1)