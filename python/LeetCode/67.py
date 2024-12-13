
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_length = max(len(a), len(b))
        a = a.zfill(max_length)  # "00123"
        b = b.zfill(max_length)  # "12345"
        
        a_ = list(map(int,a[::-1]))
        b_ = list(map(int,b[::-1]))
        
        ans = []
        ans_ = []
        for i in range(max_length):
            ans.append(0)

        carry = 0

        for i in range(max_length):
            z = a_[i] + b_[i] + carry
            match z:
                case 0:
                    ans[i] = 0
                    carry = 0
                case 1:
                    ans[i] = 1
                    carry = 0                                                                 
                case 2:
                    ans[i] = 0
                    carry = 1
                case 3:
                    ans[i] = 1
                    carry = 1
        if carry:
            ans.append(1)
        
        return "".join(map(str,ans[::-1]))
                    
                
            
            


if __name__ == "__main__":
    
    f = Solution()

    a,b = "1010","1011"

    print(f.addBinary(a,b))


"""
2つの2進数の文字列 `a` と `b` が与えられます。*それらの和を2進数の文字列として*返してください。

**例 1:**
```
入力: a = "11", b = "1"
出力: "100"
```

**例 2:**
```
入力: a = "1010", b = "1011"
出力: "10101"
```

**制約:**
* `1 <= a.length, b.length <= 104`
* `a` と `b` は `'0'` または `'1'` の文字のみで構成されています。
* 各文字列は、0自体を除いて、先頭に0を含みません。

より分かりやすく補足すると：
- 2進数の足し算を行います（例：11(2進数) + 1(2進数) = 100(2進数)）
- 入力も出力も文字列として扱います
- 必要に応じて繰り上がりの処理が必要です
"""