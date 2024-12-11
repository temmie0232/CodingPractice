
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        i = 0
        
        # if len(haystack) < len(needle):
        #     return -1

        for char in haystack:
            if char == needle[0]:
                if haystack[i:i+n] == needle:
                    return i
            i+=1

        # for i in range(len(haystack)):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i

        return -1
                
        
if __name__ == "__main__":
    
    a = Solution()
    
    haystack = "leeeee"
    needle = "sad"
    
    print(a.strStr(haystack,needle))