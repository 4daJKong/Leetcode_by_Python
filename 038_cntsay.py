
def countAndSay(n):
    if n == 1:
        return '1'
    if n == 2:
        return '11'
    str1 = '11'
    j = 3
    while (j <= n):
        
        m = len(str1)
        str2 = ''
        temp = str1[0]
        cnt = 1
        for i in range (1, m):    
            if str1[i] == temp:
                cnt = cnt + 1
            else:
                str2 = str2 + str(cnt)
                str2 = str2 + temp
                cnt = 1
                temp = str1[i]
            if i == m - 1:
                str2 = str2 + str(cnt)
                str2 = str2 + temp
        str1 = str2
        j = j + 1

    return str2


def countAndSay_demo(n):
    if n <= 0:
        return ''
    res = '1'
    
    while n > 1:
        cur = ''
        i = 0
        while i < len(res):
            cnt = 1
            while (i + 1 < len(res) and res[i] == res[i + 1]):
                cnt = cnt + 1
                i = i + 1
            cur = cur + str(cnt)
            cur = cur + str(res[i])
            i = i + 1
        res = cur
        n = n - 1
    return res



def countAndSay_demo2(n):
    if n == 0:
        return ''
    res = '1'
    while n != 1:
        res_len, i = len(res), 1
        tmp = ''
        while i <= res_len:
            count = 1
            while i < res_len and res[i] == res[i-1]:
                count += 1
                i += 1
            tmp += str(count) + str(res[i-1])
            i += 1
        res = tmp
        n -= 1    
    return res

print(countAndSay_demo(6))





