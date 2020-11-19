/**
 * Write a program to accept name and age of a person from the command prompt(passed as arguments when you execute the class) and ensure that the age entered is >=18 and < 60. 
Display proper error messages. 
The program must exit gracefully after displaying the error message in case the arguments passed are not proper. (Hint : Create a user defined exception class for handling errors.)
 */


import java.lang.Exception;

class UserException extends Exception {
    public String toString() {
        return "User Expcetion : Username or age you entered are invalid";
    }
}

class LabProgram {
    public static void main(String[] args) {

        try {

            String username = args[0];
            int age = Integer.parseInt(args[1]);
            
            if (age >=18 && age < 60 ) {
                System.out.println("Your name : "+username+ " and age : "+age+ " is valid");
            }else{
                throw new UserException();
            }

        }catch(UserException exception) {

            System.out.print(exception.toString());

        }catch(Exception exception) {

            System.out.print(exception.toString());   

        }

    }
}