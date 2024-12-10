class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char != brackets[stack.pop()]:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
                    

s = input()
a = Solution()
print(a.isValid(s))

"""

文字列 s が '('、')'、'{'、'}'、'['、']' のみで構成されているとき、その入力文字列が有効かどうかを判定してください。
入力文字列が以下の条件を満たすとき、有効とみなされます：

開きカッコは必ず同じ種類の閉じカッコで閉じられなければなりません。
開きカッコは正しい順序で閉じられなければなりません。
すべての閉じカッコには、同じ種類の対応する開きカッコが存在しなければなりません。

例 1:
入力: s = "()"
出力: true
例 2:
入力: s = "()[]{}"
出力: true
例 3:
入力: s = "(]"
出力: false
例 4:
入力: s = "([])"
出力: true
制約:

1 <= s.length <= 104
s は括弧 '()[]{}' のみで構成されます。

"""