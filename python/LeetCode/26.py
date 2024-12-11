from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0    
        while i<(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
                i -= 1
            i += 1
        return len(nums)
            
if __name__ == "__main__":
    list = [1,2,3,3,5,5,5,5,6,7,7,8]
    a = Solution()
    print(a.removeDuplicates(list))

    
"""

**問題：ソート済み配列から重複を削除する**

**やること：**
1. すでにソートされている配列から、重複している数字を削除する
2. 元の順序を保ったまま、一つの数字は一回だけ残す
3. 処理後の配列の長さを返す

**重要なポイント：**
- 配列は直接変更する（新しい配列は作らない）
- 最初の部分に重複のない数字を詰める
- 後ろの部分は何が入っていても良い

**具体例：**
```
入力: [0,0,1,1,1,2,2,3,3,4]
↓ 重複を削除
出力: [0,1,2,3,4,_,_,_,_,_]
返す値: 5（重複のない数字の個数）
```

**制約：**
- 配列は小さい順に並んでいる
- 配列の長さは1以上
- 数字は-100から100の範囲

"""