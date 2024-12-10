
def jadge(s,p):
    list_s = list(s)
    list_p = list(p)
    # pの文字数
    n = len(p)
    # sの文字数回
    for i in range(len(s)):
        # 合ってる文字数
        count = 0
        # pの文字数回
        for j in range(n):
            # sとpの文字が一緒なら
            if list_s[j] == list_p[j]:
                count += 1
                
            # 違うなら次(sの変形)
            else:
                break
        # 先頭の文字を後ろに
        if count == len(p):
            return True
        else:
            head=list_s.pop(0)
            list_s.append(head)
            

s = input()
p = input()

print("Yes") if jadge(s,p) else print("No")