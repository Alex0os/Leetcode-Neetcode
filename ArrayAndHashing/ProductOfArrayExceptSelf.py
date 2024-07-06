class Solution(object):
    def productExceptSelf(self, nums):
        nums_size = len(nums)

        results = [1]
        postfix = 1


        for num in nums:
            results.append(results[-1] * num)

        # Sucede que al final se coloca el producto de todos los numeros, lo
        # cual hace que la lista sea mas larga de lo que deberia, asi que hay
        # sacarlo

        results.pop()

        for i in range(nums_size - 1, -1, -1):
            results[i] *= postfix
            postfix *= nums[i]

        return results



print(Solution().productExceptSelf([-1,1,0,-3,3]))
