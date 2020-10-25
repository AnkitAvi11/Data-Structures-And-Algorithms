package factorial;

public class Factorial {

    public long calculateFactorial(long num) {
        if (num <= 1)
            return num;

        return num*calculateFactorial(num-1);
    }

}

