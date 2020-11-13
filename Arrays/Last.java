
class UserException extends Exception {

    public UserException(){
        
    }

    public String toString() {
        return "You have entered an invalid name or age";
    }
}

public class Last {

    public static void main(String[] args) {
        String name = args[0];
        int age = Integer.parseInt(args[1]);

        try {
            if(age >=18 && age<60) {
                System.out.println("Valid name and age entered");
            }else{
                throw new UserException();
            }
        }catch(UserException exception) {
            System.out.println("Exception found = " + exception.toString());
        }
        
    }
    
}
