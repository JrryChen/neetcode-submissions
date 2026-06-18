class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        '''
        Catlan number
        choose a person k to shake between 1 and k -> this devides the circle into two sides
            everyone between 1 -> k have to pair between themselves
            everyone btween k + 1 -> numPeople have to pair between themselves
            this becomes two smaller problems that are basically the same!

        left side contains k people
        right side has numPeople - k - 1
        we can multiple the two sides
        set k = 2i + 1 since k must be an even number
        '''
        MOD = 10 ** 9 + 7
        n = numPeople // 2
        dp = [0] * (n + 1)
        dp[0] = 1

        for pairs in range(1, n + 1):
            for left_side in range(pairs):
                dp[pairs] = dp[pairs] + dp[left_side] * dp[pairs - left_side - 1]
        return dp[n] % MOD        