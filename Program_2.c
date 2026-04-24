//Write a C program to analyze time complexities in constant time, linear time and quadratic time.
// Increase the size of input to check the time consumed

#include <stdio.h>
#include <time.h>

/* O(1) Time and Space */
void constantOperation()
{
    int a = 10, b = 20, c;
    c = a + b;
}

/* O(n) Time, O(1) Space */
void linearOperation(int n)
{
    int sum = 0;
    for(int i = 0; i < n; i++)
        sum += i;
}

/* O(n^2) Time, O(1) Space */
void quadraticOperation(int n)
{
    int sum = 0;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            sum += i + j;
}

int main()
{
    int n;
    clock_t start, end;
    double time_taken;

    printf("Enter input size: ");
    scanf("%d", &n);

    printf("\n--- Time & Space Complexity Analysis ---\n");

    /* O(1) */
    start = clock();
    constantOperation();
    end = clock();
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    printf("\nO(1) Constant Operation\n");
    printf("Time Taken  : %lf seconds\n", time_taken);
    printf("Space Used  : %lu bytes\n", 3 * sizeof(int));

    /* O(n) */
    start = clock();
    linearOperation(n);
    end = clock();
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    printf("\nO(n) Linear Operation\n");
    printf("Time Taken  : %lf seconds\n", time_taken);
    printf("Space Used  : %lu bytes\n", 2 * sizeof(int));

    /* O(n^2) */
    start = clock();
    quadraticOperation(n);
    end = clock();
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    printf("\nO(n^2) Quadratic Operation\n");
    printf("Time Taken  : %lf seconds\n", time_taken);
    printf("Space Used  : %lu bytes\n", 3 * sizeof(int));

    return 0;
}
