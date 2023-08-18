def minSubString(s, t):
    i, j = 0, 0
    m = len(s)
    n = len(t)
    maxlen = 10**5

    if m < n:
        return ""
    if m == n:
        return s

    helpDict = {}

    for ele in t:
        if ele not in helpDict:
            helpDict[ele] = 1
        else:
            helpDict[ele] += 1

    count = len(helpDict)
    ans = ""

    while j < m:  # Corrected loop condition to iterate through s
        if s[j] in helpDict:
            helpDict[s[j]] -= 1
            if helpDict[s[j]] == 0:
                count -= 1

        while count == 0:
            curlen = j - i + 1
            if curlen < maxlen:
                ans = s[i: j+1]
                maxlen = curlen

            if s[i] in helpDict:
                helpDict[s[i]] += 1
                if helpDict[s[i]] == 1:
                    count += 1
            i += 1
        j += 1

    return ans

str = "ADOBECODEBANC"
t = "ABC"
print(minSubString(str, t))
