class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        

        nxt = None
        left = 0
        max_sub_arr = 1

        for right in range(1, len(arr)):

            if nxt is None:

                if arr[right] > arr[right-1]:
                    nxt = "less"
                elif arr[right] < arr[right-1]:
                    nxt = "greater"
                else:
                    left = right

            elif arr[right] == arr[right-1]:
                nxt = None
                left = right

            else:

                if nxt == "greater":

                    if arr[right] < arr[right-1]:
                        left = right - 1
                    else:
                        nxt = "less"
                else:

                    if arr[right] > arr[right-1]:
                        left = right - 1
                    else:
                        nxt = "greater"
            
            max_sub_arr = max(max_sub_arr, right-left+1)
            
        return max_sub_arr
            


