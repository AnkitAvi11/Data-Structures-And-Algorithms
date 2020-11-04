/**

PROBLEM STATEMENT
-----------------
Implement an algorithm to determine if a string has all unique characters. 

example : 

    string = "ankit" => yes
    string = "ankita" => no

Level : medium why ?
timecomplexity = O(n)


using a hashtable 

ASCII of A = 65 - 65 is = 0
        B = 66 - 65 = 1
        c = 2
        ... z = 25

int[] arr = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] space complexity = O(26) is constanct so it becomes O(1)

for each_character in the string : 
    char ch = each_character.toUpperCase()

    if arr[ascii(character) - 65] == 0 : 
        arr[ascii(character) - 65] = 1
    else : 
        return False
 
*/

public class Unique {
    public static void main(String[] args) {
        String str = "priyaa"; 

        int[] arr = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        
        boolean flag = true;

        str = str.toUpperCase();

        for(int i=0;i<str.length();i++){
            try {
                if(arr[(int)str.charAt(i) - 65] == 1) {
                    flag = false;
                    break;
                }else{
                    arr[(int)str.charAt(i) - 65] = 1;
                }
            }catch(Exception e) {
                System.out.println("Complete");        
            }
        }

        if(flag) {
            System.out.println("The string is unique");
        }else{
            System.out.println("The string is not unique");
        }

    }
}