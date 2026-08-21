# Longest Common Subsequence (LCS) using Dynamic Programming

# Input
X = input("Enter first sequence: ")
Y = input("Enter second sequence: ")

m = len(X)
n = len(Y)

# Create DP table
dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]

# Fill the DP table
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if X[i - 1] == Y[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + X[i - 1]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

# Output
lcs = dp[m][n]

print("LCS:", lcs)
print("Length of LCS:", len(lcs))