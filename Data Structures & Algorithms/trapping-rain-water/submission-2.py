class Solution:
    def trap(self, h: list[int]) -> int:
        l,r,lm,rm,ans=0,len(h)-1,0,0,0
        while l<r:
            if h[l]<=h[r]:
                lm=max(lm,h[l])
                ans+=lm-h[l]
                l+=1
            else:
                rm=max(rm,h[r])
                ans+=rm-h[r]
                r-=1
        return ans