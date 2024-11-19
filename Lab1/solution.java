import java.time.Duration;
import java.time.Instant;

public class Main {
    public static void main(String[] args) {
        double sum = 0;
        double partialSum = 0;
        long num = 1;

        Instant startTime = Instant.now();

        while (true) {
            partialSum = 1.0 / (num * num);
            if ((partialSum + sum) == sum) {
                System.out.println("Number: " + num);
                break;
            } else {
                sum += partialSum;
                num += 1;
            }
        }

        Instant endTime = Instant.now();
        Duration executionTime = Duration.between(startTime, endTime);

        System.out.println("Execution time: " + executionTime.toNanos() / 1_000_000_000.0 + " seconds");        System.out.println("Total sum: " + sum);

        double analytical = Math.pow(Math.PI, 2) / 6;
        System.out.println("Analytical value is: " + analytical);

        double relativePercentageDifference = ((analytical - sum) / analytical) * 100;
        System.out.println("Relative percentage difference is: " + String.format("%.15f", relativePercentageDifference) + "%");    }
}