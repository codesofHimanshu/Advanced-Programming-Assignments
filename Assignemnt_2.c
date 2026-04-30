#include <stdio.h>
#include <stdlib.h>

// Function to display memory properly
void displayMemory(long bytes) {
    printf("   Memory Used: %ld bytes (%.2f KB, %.2f MB)\n",
           bytes,
           bytes / 1024.0,
           bytes / (1024.0 * 1024.0));
}

// ---------------- O(1) Space ----------------
void constantSpace() {
    int a = 10, b = 20, sum;

    sum = a + b;

    printf("\n--- Constant Space Complexity O(1) ---\n");
    printf("Operation: Sum of two numbers\n");
    printf("Result = %d\n", sum);

    long memoryUsed = 3 * sizeof(int); // a, b, sum
    displayMemory(memoryUsed);
}

// ---------------- O(n) Space ----------------
void linearSpace(int n) {
    printf("\n--- Linear Space Complexity O(n) ---\n");

    int *arr = (int *)malloc(n * sizeof(int));

    printf("Operation: Array of size %d created\n", n);

    long memoryUsed = n * sizeof(int);
    displayMemory(memoryUsed);

    free(arr);
}

// ---------------- O(n^2) Space ----------------
void quadraticSpace(int n) {
    printf("\n--- Quadratic Space Complexity O(n^2) ---\n");

    int **matrix = (int **)malloc(n * sizeof(int *));

    for (int i = 0; i < n; i++) {
        matrix[i] = (int *)malloc(n * sizeof(int));
    }

    printf("Operation: Matrix of size %d x %d created\n", n, n);

    long memoryUsed = n * n * sizeof(int);
    displayMemory(memoryUsed);

    // Free memory
    for (int i = 0; i < n; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

// ---------------- MAIN ----------------
int main() {
    int n;

    printf("Enter input size n: ");
    scanf("%d", &n);

    printf("\n=========================================\n");
    printf("     SPACE COMPLEXITY ANALYSIS PROGRAM\n");
    printf("=========================================\n");

    constantSpace();
    linearSpace(n);
    quadraticSpace(n);

    printf("\n=========================================\n");
    printf("Program Finished Successfully!\n");
    printf("=========================================\n");

    return 0;
}
