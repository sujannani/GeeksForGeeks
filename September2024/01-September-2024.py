class Solution:
    def maxPathSum(self, arr1, arr2):
        i, j = 0, 0
        result, sum1, sum2 = 0, 0, 0
        m, n = len(arr1), len(arr2)
        
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            else:
                result += max(sum1, sum2) + arr1[i]
                sum1 = sum2 = 0
                i += 1
                j += 1

        while i < m:
            sum1 += arr1[i]
            i += 1

        while j < n:
            sum2 += arr2[j]
            j += 1

        result += max(sum1, sum2)

        return result