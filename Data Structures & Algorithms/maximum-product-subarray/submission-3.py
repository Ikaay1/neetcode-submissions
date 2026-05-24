class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        def get_subs():
            res = []
            sub = []

            for num in nums:
                if num == 0:
                    if sub:
                        res.append(sub)
                        sub = []
                else:
                    sub.append(num)
            
            if sub:
                res.append(sub)
            
            return res
        
        sub_nums = get_subs()
        print(sub_nums)
        res = -float('inf')

        for sub_num in sub_nums:
            negatives = sum(num < 0 for num in sub_num)

            left = 0
            product = 1
            max_product = -float('inf')
            for right in range(len(sub_num)):
                num = sub_num[right]
                product *= num
                max_product = max(max_product, product)

                if num < 0:
                    negatives -= 1
                
                if product < 0 and not negatives:
                    while product < 0:
                        product //= sub_num[left]
                        left += 1

            res = max(res, max_product)
        
        if 0 in nums:
            return max(0, res)
        
        return res

