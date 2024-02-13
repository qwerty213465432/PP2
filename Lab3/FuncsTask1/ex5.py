def perm(s, cur=""): 
    if len(s) == 0:
        print(cur)
    else:
        for i in range(len(s)):
            nextch = s[i]
            rech = s[:i] + s[i+1:]
            perm(rech, cur + nextch)


sent = input()
perm(sent)
