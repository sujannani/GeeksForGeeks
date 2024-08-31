class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n < 3:
            return []

        smaller = [-1] * n
        greater = [-1] * n

        min_index = 0
        for i in range(1, n):
            if arr[i] <= arr[min_index]:
                min_index = i
            else:
                smaller[i] = min_index

        max_index = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[max_index]:
                max_index = i
            else:
                greater[i] = max_index

        for i in range(n):
            if smaller[i] != -1 and greater[i] != -1:
                return [arr[smaller[i]], arr[i], arr[greater[i]]]

        return []