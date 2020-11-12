
abstract class GeneralBank {

    abstract double getSavingInterestRate();
    abstract double getFixedInterestRate();
    
}

class ICICIBank extends GeneralBank {
    private double saving_rate;
    private double fixed_rate;

    public ICICIBank() {

    }

    public ICICIBank(double a, double b) {
        this.saving_rate = a;
        this.fixed_rate = b;
    }

    public double getFixedInterestRate () {
        return this.fixed_rate;
    }

    public double getSavingInterestRate() {
        return this.saving_rate;
    }

}


class KotMBank extends GeneralBank {
    private double saving_rate;
    private double fixed_rate;

    public KotMBank() {

    }

    public KotMBank(double a, double b) {
        this.saving_rate = a;
        this.fixed_rate = b;
    }

    public double getFixedInterestRate () {
        return this.fixed_rate;
    }

    public double getSavingInterestRate() {
        return this.saving_rate;
    }

}


class Bank {
    public static void main(String[] args) {
        ICICIBank ob = new ICICIBank(4.0, 8.5);
        KotMBank ob2 = new KotMBank(6.0, 9.0);
        GeneralBank ref = ob;
        System.out.println(ref.getSavingInterestRate()+" "+ref.getFixedInterestRate());
        ref = ob2;
        System.out.println(ref.getSavingInterestRate()+" "+ref.getFixedInterestRate());
    }
}