import java.util.*;

// Base Class
class Account {
    private String accountNumber;
    private String ownerName;
    private double balance;

    // Default constructor (constructor chaining)
    public Account() {
        this("0000", "Unknown", 0.0);
    }

    // Parameterized constructor
    public Account(String accountNumber, String ownerName, double balance) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        if (balance < 0) {
            throw new IllegalArgumentException("Initial balance cannot be negative");
        }
        this.balance = balance;
    }

    // Getters
    public String getAccountNumber() {
        return accountNumber;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public double getBalance() {
        return balance;
    }

    // Setters
    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }

    public void setBalance(double balance) {
        if (balance < 0) {
            throw new IllegalArgumentException("Balance cannot be negative");
        }
        this.balance = balance;
    }

    // Deposit method
    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit must be positive");
        }
        balance += amount;
        System.out.println("Deposited: " + amount);
    }

    // Withdraw method
    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal must be positive");
        }
        if (amount > balance) {
            throw new IllegalArgumentException("Insufficient balance");
        }
        balance -= amount;
        System.out.println("Withdrawn: " + amount);
    }

    // Display method
    public void display() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Owner Name: " + ownerName);
        System.out.println("Balance: " + balance);
    }
}

// SavingsAccount subclass
class SavingsAccount extends Account {
    private double interestRate;

    public SavingsAccount(String accNo, String name, double balance, double interestRate) {
        super(accNo, name, balance); // constructor chaining with super
        this.interestRate = interestRate;
    }

    public double calculateInterest() {
        return getBalance() * interestRate / 100;
    }

    @Override
    public void display() {
        super.display(); // call base method
        System.out.println("Interest Rate: " + interestRate + "%");
        System.out.println("Interest: " + calculateInterest());
    }
}

// CurrentAccount subclass
class CurrentAccount extends Account {
    private double overdraftLimit;

    public CurrentAccount(String accNo, String name, double balance, double overdraftLimit) {
        super(accNo, name, balance);
        this.overdraftLimit = overdraftLimit;
    }

    @Override
    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal must be positive");
        }
        if (amount > getBalance() + overdraftLimit) {
            throw new IllegalArgumentException("Exceeds overdraft limit");
        }
        setBalance(getBalance() - amount);
        System.out.println("Withdrawn (Current): " + amount);
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Overdraft Limit: " + overdraftLimit);
    }
}

// Main class to demonstrate polymorphism
public class Banking_system {
    public static void main(String[] args) {

        // Polymorphism: Account reference
        List<Account> accounts = new ArrayList<>();

        accounts.add(new SavingsAccount("101", "Himanshu", 5000, 5));
        accounts.add(new CurrentAccount("102", "Rahul", 2000, 1000));

        for (Account acc : accounts) {
            acc.display(); // runtime polymorphism
            System.out.println("-------------------");
        }

        // Testing validation
        try {
            accounts.get(0).withdraw(10000); // should fail
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}