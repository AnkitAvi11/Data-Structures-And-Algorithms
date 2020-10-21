"""
Problem Statement : Bill Division (Source : Hackerrank)
Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: . Anna declines to eat item  which costs . If Brian calculates the bill correctly, Anna will pay . If he includes the cost of , he will calculate . In the second case, he should refund  to Anna.

Function Description

Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.

bonAppetit has the following parameter(s):

bill: an array of integers representing the cost of each item ordered
k: an integer representing the zero-based index of the item Anna doesn't eat
b: the amount of money that Anna contributed to the bill
Input Format

The first line contains two space-separated integers  and , the number of items ordered and the -based index of the item that Anna did not eat.
The second line contains  space-separated integers  where .
The third line contains an integer, , the amount of money that Brian charged Anna for her share of the bill.

Constraints

The amount of money due Anna will always be an integer
Output Format

If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e., ) that Brian must refund to Anna. This will always be an integer.

Sample Input 0

4 1
3 10 2 9
12

Sample Output 0

5
"""

#   function for the required problem
def bonAppetite(bill : list, k : int, b : int) : 
    fair_share = 0

    #   getting the bill shared by both of them
    for i in range(0, len(bill)) : 
        if i != k : 
            fair_share += bill[i]

    #   checking if both of them paid the same amount
    if fair_share//2 == b : 
        return "Bon Appetit"

    #   if anyone of them doesnt pay the same amount
    return fair_share//2 - b


#   main section of the program
if __name__ == '__main__' : 
    print(bonAppetite([3,10,2,9], 1, 7))