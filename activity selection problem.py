##ACTIVITY SELECTION PROBLEM

def max_activities(s,f):
    l,ans=[],[]
    for i in range(len(s)):
        l1=[s[i],f[i]]
        l.append(l1)
    l=sorted(l,key=lambda x:x[1])
    i=0
    ans.append(i)
    for j in range(1,len(l)):
        if l[j][0]>=l[i][1]:
            ans.append(j)
            i=j
    return ans
        

s = [1 , 3 , 0 , 5 , 8 , 5] 
f = [2 , 4 , 6 , 7 , 9 , 9] 
print("The selected set of activities are:- ",max_activities(s , f) )
