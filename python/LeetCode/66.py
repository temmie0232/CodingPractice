
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True

        digits_reverse = digits[::-1]
        for i in digits_reverse:
            if i!=9:
                flag = False
        if flag:
            digits_reverse.append(0)
        for i in range(len(digits_reverse)):
            if digits_reverse[i] != 9:
                digits_reverse[i] += 1
                break
            else:
                digits_reverse[i] = 0
        return digits_reverse[::-1]
    
    """
    def plusOne(self, digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    return [1] + digits
    """
                

if __name__ == "__main__":
    
    a = Solution()

    digits = [8,9,9,9]

    print(a.plusOne(digits))

        
"""

整数配列 `digits` として表される**大きな整数**が与えられます。ここで、各 `digits[i]` はその整数の `i` 番目の数字です。数字は左から右の順に最上位から最下位まで並んでいます。この大きな整数は先頭に `0` を含みません。

大きな整数に1を加えて、*結果の数字の配列*を返してください。

**例 1:**
```
入力: digits = [1,2,3]
出力: [1,2,4]
説明: この配列は整数123を表します。
1を加えると 123 + 1 = 124 となります。
したがって、結果は [1,2,4] となります。
```

**例 2:**
```
入力: digits = [4,3,2,1]
出力: [4,3,2,2]
説明: この配列は整数4321を表します。
1を加えると 4321 + 1 = 4322 となります。
したがって、結果は [4,3,2,2] となります。
```

**例 3:**
```
入力: digits = [9]
出力: [1,0]
説明: この配列は整数9を表します。
1を加えると 9 + 1 = 10 となります。
したがって、結果は [1,0] となります。
```

**制約:**
* `1 <= digits.length <= 100`
* `0 <= digits[i] <= 9`
* `digits` は先頭に `0` を含みません。
"""