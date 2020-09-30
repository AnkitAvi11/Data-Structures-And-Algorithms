## If You Don't Know What A list is then: List is colllection of data that can be of any Type.
## first We Create A fucntion
def reverse_l(li):
    length= len(li)
    first=list(n.split())
    for a in range(len(first)): ## This Range Is Converting the String input into int 
        li[a]=int(first[a])
    for i in range(length//2):
        li[i],li[(length-i)-1]=li[(length-i)-1],li[i]
n=input("Enter Numbers given by space: ") ## here i Specify to Give Space otherwise 12345 will be considerd as one string not numbers and then cannot be splitted 
reverse_l(li)                             ## Program Can Be Modified With More Flexibilty 
print(li)
