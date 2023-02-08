class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l=len(s)
        count=0
        ans=[]
        for i in range(len(s)):
            if(s[i]=='I'):
                ans.append(count)
                count+=1
            else:
                ans.append(l)
                l-=1
        ans.append(x)
        return ans