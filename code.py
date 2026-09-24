class Solution:
    def greatestLetter(self, s: str) -> str:
        d={}
        for n in s:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
        u=[]
        for wo in d:
            if wo.upper() in d and wo.lower() in d:
                x=wo.upper()
                u.append(x)
        u.sort()  
        if len(u)<=0:
            return ''
        for i in range(len(u)-1,-1,-1):
            return u[i]   
        
        
