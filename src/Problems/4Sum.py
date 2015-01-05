'''
Created on 30 Dec 2014

@author: Yuan
'''

'''
In order to avoid TLE, a reduction to 2Sum can be employed.
Particularly, maintain the dictionary dict = {ni+nj:[[i,j]]}
Then use 2 pointers:
1. p1 in range(1,len(num))[::-1], n1 = num[p1] as the first different element
2. p2 in range(0,p1)[::-1], n2 = num[p2] as the first different element
3. for each n1+n2, if target-(n1+n2) in dict, then 
    for each [i,j] in dict[target - (n1+n2)]: if j < p2, then we find a solution
'''


class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    
    # recursive solution, TLE
    def fourSum1(self, num, target):
        result = []
        current = []
        num.sort()
        self.NSum(num, target, 4, 0, result, current)
        return result
        
    def NSum(self, num, target, N, start, result, current):
        if N == 0:
            if target == 0:
                result.append(current)
            return
        if len(num)-start < N:
            return
        for i in range(start,len(num)):
            if i > start and num[i] == num[i-1]:
                i += 1
            elif num[i]*N <= target:
                self.NSum(num, target-num[i], N-1, i+1, result, current+[num[i]])
            else:
                return

    
    
    # this solution is slightly simpler with reduction to 2-sum.        
    def fourSum(self, num, target):
        if len(num) < 4:
            return [];
        dict = {}
        result = []
        num.sort();
        for i in range(len(num)):
            if i == 0 or num[i] > num[i-1]:
                if num[i] * 4<= target:
                    for j in range(i+1, len(num)):
                        if j == i+1 or num[j] > num[j-1]:
                            if num[i]+ num[j]*3 <= target:
                                sum = num[i]+num[j]
                                if sum in dict:
                                    dict[sum].append([i,j])
                                else:
                                    dict[sum] = [[i,j]]
                            else:
                                break
                else:
                    break
        for k in range(1,len(num))[::-1]:
            if k == len(num)-1 or num[k]<num[k+1]:
                for l in range(0,k)[::-1]:
                    if l == k-1 or num[l]< num[l+1]:
                        sum = num[k]+num[l]
                        if target -sum in dict:
                            for pair in dict[target-sum]:
                                if pair[1]<l:
                                    result.append([num[pair[0]], num[pair[1]], num[l], num[k]])
        return result                  

sol = Solution()

print sol.fourSum([1,0,-1,0,-2,2,2], 0)