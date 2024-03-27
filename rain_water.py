'''Trapped rain water

Given with n non-negative integers representing an elevation map where the width of
each bar is 1, we need to compute how much water it is able to trap after raining.'''

def calcRain(arr):
    water=[0]*len(arr)
    for i in range(1, len(arr)-1):
        water[i]=min(max(arr[:i]), max(arr[i+1:])) - arr[i]
        if(water[i])<0:
            water[i]=0

    return sum(water)

def main():
    elevations = list(map(int, input().split()))
    print(calcRain(elevations))

if __name__=='__main__':
    main()
