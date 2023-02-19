import time


def isPalindrom(s):
    #count = 0
    start = time.time()
    for i in range(int(len(s)/2)):
        if s[i] != s [len(s)-i-1]:
            #count += 1
            end = time.time()
            print((end - start) * 10 ** 3)
            return False
    else:
        end = time.time()
        return True

def isPalindrom2(s):
    #if len(s) == 0:
    if not len(s):
        return True
    else:
        return s[0] == s[-1] and isPalindrom2(s[1:-1])


print(isPalindrom("топот"))
print(isPalindrom2("шалаш"))