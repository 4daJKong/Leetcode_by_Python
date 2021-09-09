def strStr(haystack, needle):
   
    if needle == "" or needle == haystack:
        return 0
 
    n = len(needle)
    m = len(haystack)
    for j in range(0, m - n + 1):
        #print(j)
        for i in range(0, n):
            
            if needle[i] != haystack[j + i]:
                break
            elif i == n - 1:
                return j
      
    return -1

print(strStr("mississippi","pi"))

print(strStr("mississippi","issip"))
print(strStr("aaaaa", "bba"))
print(strStr("a", "a"))
print(strStr("hello", "ll"))
print(strStr("hekmo", "km"))
print(strStr("GoldenGlobalView", "lob"))
print(strStr("string1 onexxx string2 on yyy ", "yyy"))
print(strStr("go simple string", "go"))



def strStr_demo1(haystack, needle):
    M, N = len(haystack), len(needle)
    for i in range(M - N + 1):
        if haystack[i : i + N] == needle:
            return i
    return -1

 
def strStr_demo2(haystack, needle):

    return haystack.find(needle)