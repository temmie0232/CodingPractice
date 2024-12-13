
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        array = s.split()
        return len(array[-1])
            
        
if __name__ == "__main__":
    a = Solution()
    s = "fly me to the moon"

    print(a.lengthOfLastWord(s))

    
"""

文字列 `s` が与えられます。文字列は単語とスペースで構成されています。文字列の**最後**の単語の*長さ*を返してください。
**単語**とは、スペース以外の文字のみで構成される最大の部分文字列のことです。

**例 1:**
```
入力: s = "Hello World"
出力: 5
説明: 最後の単語は "World" で、長さは5です。
```

**例 2:**
```
入力: s = "   fly me   to   the moon  "
出力: 4
説明: 最後の単語は "moon" で、長さは4です。
```

**例 3:**
```
入力: s = "luffy is still joyboy"
出力: 6
説明: 最後の単語は "joyboy" で、長さは6です。
```

**制約:**
* `1 <= s.length <= 104`
* `s` は英字とスペース `' '` のみで構成されます。
* `s` には少なくとも1つの単語が含まれます。

"""