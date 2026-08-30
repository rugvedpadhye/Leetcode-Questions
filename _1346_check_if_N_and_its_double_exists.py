class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j]==2*arr[i] and i!=j:
                    return True
        return False