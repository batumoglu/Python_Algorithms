class Solution:
    def reverseBits(self, n):
        binary = bin(n)[2:]
        binary = binary.zfill(32)
        binary = binary[::-1]
        return int(binary, 2)

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseBits(56743))