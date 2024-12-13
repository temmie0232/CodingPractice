
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: # type: ignore  戻り値がNoneの可能性あり
        if not nums:
            return 0
        x = 0
        for i in nums:
            if i == target:
                return x
            x+=1
        y = 0
        for j in nums:
            if j > target:
                return y
            y+=1
            if j == nums[-1]:
                return y

        """
        for i,num in enumerate(nums):
            if num > target:
                return i
        return len(nums)
        """

if __name__ == "__main__":
    
    a = Solution()

    nums = [1,3,5,6]
    target = 7

    print(a.searchInsert(nums,target))
    

"""

問題: ソート済みの異なる整数の配列とターゲット値が与えられたとき、ターゲットが見つかればそのインデックスを返します。見つからなければ、それが挿入されるべきインデックスを返します。アルゴリズムの実行時間の複雑度は O(log n) である必要があります。

例:

入力: nums = [1,3,5,6], target = 5

出力: 2

入力: nums = [1,3,5,6], target = 2

出力: 1

入力: nums = [1,3,5,6], target = 7

出力: 4

制約:

1 <= nums.length<= 10^4

-10^4 <= nums[i] <= 10^4

nums は昇順にソートされた異なる値を含む

-10^4 <= target <= 10^4
"""