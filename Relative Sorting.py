"""
Given two arrays A1[] and A2[] of size N and M respectively. The task is to sort A1 in such a way that the relative order among the elements will be same as those in A2. For the elements not present in A2, append them at last in sorted order. It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.
Note: Expected time complexity is O(N log(N)).

Input:
First line of input contains number of testcases. For each testcase, first line of input contains length of arrays N and M and next two line contains N and M elements respectively.

Output:
Print the relatively sorted array.

Constraints:
1 ≤ T ≤ 100
1 ≤ N,M  ≤ 106
1 ≤ A1[], A2[] <= 106

Example:
Input:
2
11 4
2 1 2 5 7 1 9 3 6 8 8
2 1 8 3
8 4
2 6 7 5 2 6 8 4 
2 6 4 5
Output:
2 2 1 1 8 8 3 5 6 7 9
2 2 6 6 4 5 7 8

Explanation:
Testcase 1: After sorting the resulted output is 2 2 1 1 8 8 3 5 6 7 9.
Testcase 2: After sorting the resulted output is 2 2 6 6 4 5 7 8.
"""

t= int(input())
i = 0

while t>0:
    n1, n2 = map(int, input().split())

    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    d1 = {}

    for i in l1:
        d1[i] = 0

    for i in l1:
        d1[i] = d1[i] + 1
        
    x = []
    o=[]
    j = 0
    leftElements=[]

    for i in range(0, n2):
        if l2[i] in l1 :
            if l2[i] not in o:


                    x+=[l2[i]]*d1[l2[i]]
                    o.append(l2[i])
                    j=j+1


    sortedList=[]
    for i in l1:
        if i not in x:
            sortedList.append(i)
    sortedList.sort()
    for i in sortedList:
        x.append(i)

    s=""
    for i in x:
        s=s+str(i)+" "
    print(s)
    t=t-1
