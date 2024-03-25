# Leetcode - Two Sum
# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return None


# question
def main():
    nums = [2, 17, 11, 7]
    target = 18

    solution = Solution()
    result = solution.twoSum(nums, target)
    print("Indices of the two numbers:", result)


if __name__ == "__main__":
    main()
