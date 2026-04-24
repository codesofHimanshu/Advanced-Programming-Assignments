//Write a C program to analyze time complexities in constant time, linear time and quadratic time.
// Increase the size of input to check the time consumed

#include <stdio.h>
#include <time.h>

void constantTime() {
    int a = 10, b = 20, c;
    c = a + b;   // O(1)
}

void linearTime(int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {   // O(n)
        sum += i;
    }
}

void quadraticTime(int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {       // O(n^2)
        for (int j = 0; j < n; j++) {
            sum += i + j;
        }
    }
}

int main() {
    clock_t start, end;
    double time_taken;
    int n;

    printf("Enter input size: ");
    scanf("%d", &n);

    // Constant Time
    start = clock();
    constantTime();
    end = clock();
    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Constant Time (O(1)): %f seconds\n", time_taken);

    // Linear Time
    start = clock();
    linearTime(n);
    end = clock();
    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Linear Time (O(n)): %f seconds\n", time_taken);

    // Quadratic Time
    start = clock();
    quadraticTime(n);
    end = clock();
    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Quadratic Time (O(n^2)): %f seconds\n", time_taken);

    return 0;
}
