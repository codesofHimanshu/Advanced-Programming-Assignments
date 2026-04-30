import java.util.*;
import java.util.stream.*;

class Student {
    int id;
    String name;
    List<String> courses;
    Map<String, Integer> scores;

    public Student(int id, String name, List<String> courses, Map<String, Integer> scores) {
        this.id = id;
        this.name = name;
        this.courses = courses;
        this.scores = scores;
    }

    // Calculate average score
    public double getAverageScore() {
        return scores.values()
                .stream()
                .mapToInt(Integer::intValue)
                .average()
                .orElse(0.0);
    }

    @Override
    public String toString() {
        return name + " (Avg: " + getAverageScore() + ")";
    }
}

public class Main {

    // 1. Top N Students
    public static List<Student> getTopNStudents(List<Student> students, int n) {
        return students.stream()
                .sorted(Comparator.comparingDouble(Student::getAverageScore).reversed())
                .limit(n)
                .collect(Collectors.toList());
    }

    // 2. Average per course
    public static Map<String, Double> getAverageScorePerCourse(List<Student> students) {

        Map<String, List<Integer>> temp = new HashMap<>();

        for (Student s : students) {
            for (String course : s.courses) {
                int score = s.scores.getOrDefault(course, 0); // handle missing
                temp.computeIfAbsent(course, k -> new ArrayList<>()).add(score);
            }
        }

        Map<String, Double> avgMap = new HashMap<>();

        for (String course : temp.keySet()) {
            List<Integer> scores = temp.get(course);

            double avg = scores.stream()
                    .mapToInt(Integer::intValue)
                    .average()
                    .orElse(0.0);

            avgMap.put(course, avg);
        }

        return avgMap;
    }

    // 3. Unique courses
    public static Set<String> getAllUniqueCourses(List<Student> students) {
        return students.stream()
                .flatMap(s -> s.courses.stream())
                .collect(Collectors.toSet());
    }

    public static void main(String[] args) {

        List<Student> students = new ArrayList<>();

        // ---- Sample Data ----
        students.add(new Student(
                1,
                "Himanshu",
                Arrays.asList("DSA", "Math", "OS"),
                new HashMap<>(Map.of("DSA", 90, "Math", 85, "OS", 80))
        ));

        students.add(new Student(
                2,
                "Rahul",
                Arrays.asList("DSA", "Math"),
                new HashMap<>(Map.of("DSA", 70, "Math", 75))
        ));

        students.add(new Student(
                3,
                "Ankit",
                Arrays.asList("DSA", "OS"),
                new HashMap<>(Map.of("DSA", 95, "OS", 88))
        ));

        // ---- Add more data (to see real time difference) ----
        for (int i = 4; i <= 100000; i++) {
            students.add(new Student(
                    i,
                    "Student" + i,
                    Arrays.asList("DSA", "Math", "OS"),
                    new HashMap<>(Map.of("DSA", 80, "Math", 70, "OS", 60))
            ));
        }

        // -------- Measure Sorting Time --------
        long startSort = System.nanoTime();

        List<Student> topStudents = getTopNStudents(students, 5);

        long endSort = System.nanoTime();

        System.out.println("Top Students:");
        topStudents.forEach(System.out::println);

        System.out.println("Sorting Time: " + (endSort - startSort) + " ns");


        // -------- Measure Course Average Time --------
        long startAvg = System.nanoTime();

        Map<String, Double> avgCourse = getAverageScorePerCourse(students);

        long endAvg = System.nanoTime();

        System.out.println("\nAverage Score Per Course:");
        avgCourse.forEach((k, v) -> System.out.println(k + " -> " + v));

        System.out.println("Average Calculation Time: " + (endAvg - startAvg) + " ns");


        // -------- Unique Courses --------
        long startSet = System.nanoTime();

        Set<String> courses = getAllUniqueCourses(students);

        long endSet = System.nanoTime();

        System.out.println("\nUnique Courses: " + courses);

        System.out.println("Unique Course Extraction Time: " + (endSet - startSet) + " ns");


        // -------- Complexity Info (Printed) --------
        int N = students.size();
        int C = courses.size();

        System.out.println("\n--- Complexity Analysis ---");
        System.out.println("Course Average: O(N * C)");
        System.out.println("Sorting Top N: O(N log N)");
        System.out.println("Where N = " + N + ", C = " + C);
    }
}