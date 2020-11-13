
def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def smallestDivNumber(num) : 
    lcm = compute_lcm(1,2)

    for i in range(3, num+1) :
        lcm = compute_lcm(lcm, i)

    return lcm



if __name__ == '__main__' : 
    print(smallestDivNumber(3))