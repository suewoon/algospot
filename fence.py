# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 01:15:01 2017

@author: suewoonryu
"""
import sys

"""
3
7
7 1 5 9 6 7 3
7
1 4 4 4 4 1 1 
4
1 8 2 2 
"""
#todo : read lines from input and call methods 
def main():
    testCases = int(sys.stdin.readline()) # testcase <= 50 
    for i in range(0, testCases*2,2):
        xrange = int(sys.stdin.readline())
        global heights 
        heights = []
        for i in sys.stdin.readline().split():
            heights.append(int(i))
        print(getMaxArea(0,xrange-1))
        
#do bisection search..
def getMaxArea(left, right):
    maxArea = 0
    print('left'+str(left)+'right'+str(right))
    if left - right == 0:
        return heights[left]
    mid = int(left+right/2)
    maxArea = max(getMaxArea(left,mid),getMaxArea(mid+1,right))

    #when a rectangle spans from the middle ..
    span_left = mid
    span_right = mid+1
    minHeight = min(heights[span_left], heights[span_right])
    maxArea = max(maxArea, minHeight*(span_right-span_left))
    
    #expand a rectangle 'til it can 
    while left < span_left and span_right < right : 
        if heights[span_left-1] < heights[span_right+1] or span_left==left:
            span_right+=1
            minHeight = min(right, heights[span_right])
        else:
            span_left-=1
            minHeight = min(left, heights[span_left])
        maxArea = max(maxArea, (span_right-span_left)*minHeight)
        
    return maxArea

if '__name__' == '__main__' : main()