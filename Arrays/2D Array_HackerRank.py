def hourglassSum(arr):
    maxsum=-63
    for i in range(4):
        for j in range(4):
            top=sum(arr[i][j:j+3])
            mid=arr[i+1][j+1]
            bottom=sum(arr[i+2][j:j+3])
            hourglass =top+mid+bottom
            if hourglass>maxsum:
                maxsum=hourglass
    return maxsum
Test_cases=int(input())
while t>0:
   n=int(input("Size of The Array"))
   arr=[int(x) for x in input().split()]
   print(hourglassSum(arr))
   t-=1
